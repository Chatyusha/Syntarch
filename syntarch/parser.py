from typing import Union
from typing import Any

from .token import Token
from .marker import Marker
from .types import TokenTypes, TokenValues
from pathlib import Path


class Parser(object):
    read_text: str
    converted_text: list[str] = []
    pre_syntax_tree: list[Token] = []
    syntax_tree = []
    marker: Union[Marker, Any]
    tmp_syntax: str

    def __init__(self,marker = None,types = None):
        if marker:
            self.marker = marker
        else:
            self.marker = Marker()
        if types:
            self.types = types
        else:
            self.types = TokenTypes()
            self.values = TokenValues()
    
    def read_file(self,file_path: str):
        self.read_text = Path(file_path).read_text()
        self.converted_text = self.read_text.split("\n\n")
        
    def pre_process(self):
        while self.converted_text:
            block = self.converted_text.pop(0)
            _contents : list[str] = [] 
            token = Token()
            if self.marker.RE_HEAD.search(block):
                token.type = self.types.TYPE_HEAD
                _contents.append(block)
            elif self.marker.RE_START_CODE_BLOCK.search(block):
                token.type = self.types.TYPE_CODE_BLOCK
                while not self.marker.RE_END_CODE_BLOCK.search(block):
                    _contents.append(block)
                    block = self.converted_text.pop(0)
                else:
                    _contents.append(block)
            elif self.marker.RE_QUOTE_BLOCK.search(block):
                token.type = self.types.TYPE_QUOTE_BLOCK
                _contents.append(block)
            elif self.marker.RE_TABLE.search(block):
                token.type = self.types.TYPE_TABLE
                _contents.append(block)
            elif self.marker.RE_DISPLAY_MATH.search(block):
                token.type = self.types.TYPE_DISPLAY_MATH
                _contents.append(block)
            elif self.marker.RE_DOT_LIST.search(block):
                token.type = self.types.TYPE_DOT_LIST
                _contents.append(block)
            else:
                token.type = self.types.TYPE_PARAGRAPH
                _contents.append(block)
            token.contents = "\n\n".join(_contents)
            self.pre_syntax_tree.append(token)

    def build_head(self, contents):
        token = Token()
        token.type = self.types.TYPE_HEAD
        # "#"のベタ打ちはそのうち直す
        # より抽象度の高いコードに変更(そのうち)
        token.level = self.marker.RE_HEAD.match(contents).group().count("#")
        token.contents = contents[token.level:]
        return token
    
    def build_code_block(self,contents: str):
        token = Token()
        token.type = self.types.TYPE_CODE_BLOCK
        _contents = list(filter(None,self.marker.RE_CODE_BLOCK_MARK.sub("",contents).split("\n")))
        token.language = _contents.pop(0)
        token.contents = "\n".join(_contents)
        return token
    
    def build_quote_block(self,contents : str):
        token = Token()
        token.type = self.types.TYPE_QUOTE_BLOCK
        _contents = self.marker.RE_QUOTE_LINE.sub("",contents)
        token.children = self.build_context(_contents)
        return token

    
    def build_paragraph(self,contents):
        paragraph = Token()
        paragraph.type = self.types.TYPE_PARAGRAPH
        paragraph.children =  self.build_context(contents)
        return paragraph

    def build_context(self,contents):
        match_iter = self.marker.RE_CONTEXT.finditer(contents)
        syntax :list[Token] = []
        for match in match_iter:
            match_text = match.group()
            token = Token()
            if part:=self.marker.RE_NEW_LINE.match(match_text):
                token.type = self.types.TYPE_NEW_LINE
            elif part:=self.marker.RE_EMPHASIS.match(match_text):
                token.type = self.types.TYPE_EMPHASIS
            elif part:=self.marker.RE_ITALIC.match(match_text):
                token.type = self.types.TYPE_ITALIC
            elif part:=self.marker.RE_INLINE.match(match_text):
                token.type = self.types.TYPE_INLINE
            elif part:=self.marker.RE_INLINE_MATH.match(match_text):
                token.type = self.types.TYPE_INLINE_MATH
            elif part:=self.marker.RE_PLAINE.match(match_text):
                token.type = self.types.TYPE_PLAINE
            token.contents = part.group(0)
            syntax.append(token)
        return syntax
    
    def build_table(self,contents : str):
        table = Token()
        table.type = self.types.TYPE_TABLE
        contents_matrix = [list(filter(None, row.split("|"))) for row in contents.split("\n")]
        table.children.append(self.build_table_row(contents_matrix.pop(0)))
        table.children.append(self.build_table_position(contents_matrix.pop(0)))
        for row in contents_matrix:
            table.children.append(self.build_table_row(row))
        return table
    
    def build_table_row(self,row : list[str]):
        token = Token()
        token.type = self.types.TYPE_TABLE_ROW
        for cell in row:
            _cell = Token()
            _cell.type = self.types.TYPE_TABLE_CELL
            _cell.children = self.build_context(cell)
            token.children.append(_cell)
        return token
    
    def build_table_position(self,positions : list[str]):
        token = Token()
        token.type = self.types.TYPE_TABLE_POSITIONS
        for pos in positions:
            _pos = Token()
            _pos.type = self.types.TYPE_TABLE_POSITION
            if self.marker.RE_TABLE_POSITION_LEFT.match(pos):
                _pos.contents = self.values.CONST_TABLE_POSITION_LEFT
            elif self.marker.RE_TABLE_POSITION_CENTER.match(pos):
                _pos.contents = self.values.CONST_TABLE_POSITION_CENTER
            elif self.marker.RE_TABLE_POSITION_RIGHT.match(pos):
                _pos.contents = self.values.CONST_TABLE_POSITION_RIGHT
            token.children.append(_pos)
        return token
    
    def build_list(self,contents : str):
        root = Token() # rootのlevelは0
        token = Token()
        token.type = self.types.TYPE_DOT_LIST
        current_parent = root
        current_level = 0
        latest = root
        for value in contents.split("\n"):
            node = Token()
            level = 1
            while self.marker.RE_DOT_LIST_INDENT.match(value):
                value = self.marker.RE_DOT_LIST_INDENT.sub("",value)
                level += 1
            else:
                value = self.marker.RE_DOT_LIST_MARKER.sub("",value)
                node.type = self.types.TYPE_DOT_LIST
                node.children = self.build_context(value)
                if level > current_level:
                    current_parent = latest
                elif level == current_level:
                    pass
                elif level < current_level:
                    current_parent = current_parent.parent
                current_level = level
                node.parent = current_parent
                current_parent.items.append(node)
                latest = node
        token.children = root.items
        return token

    def build_markdown(self):
        self.pre_process()
        for part in self.pre_syntax_tree:
            _contents = part.contents
            if part.type == self.types.TYPE_HEAD:
                self.syntax_tree.append(self.build_head(_contents))
            elif part.type == self.types.TYPE_PARAGRAPH:
                self.syntax_tree.append(self.build_paragraph(_contents))
            elif part.type == self.types.TYPE_CODE_BLOCK:
                self.syntax_tree.append(self.build_code_block(_contents))
            elif part.type == self.types.TYPE_QUOTE_BLOCK:
                self.syntax_tree.append(self.build_quote_block(_contents))
            elif part.type == self.types.TYPE_TABLE:
                self.syntax_tree.append(self.build_table(_contents))
            elif part.type == self.types.TYPE_DOT_LIST:
                self.syntax_tree.append(self.build_list(_contents))
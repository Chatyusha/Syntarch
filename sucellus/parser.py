import re
from typing import Union
from typing import Any

from .token import Paragraph, Table
from .token import Token
from .token import Head
from .token import CodeBlock
from .token import Text
from .marker import Marker
from .types import TokenTypes
from pathlib import Path

from sucellus import types

from sucellus import codeblock

from sucellus import token

class Parser(object):
    read_text: str
    converted_text: list[str] = []
    pre_syntax_tree: list[Token] = []
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
    
    def read_file(self,file_path: str):
       self.read_text = Path(file_path).open().read()
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
            else:
                token.type = self.types.TYPE_PARAGRAPH
                _contents.append(block)
            token.contents = "\n\n".join(_contents)
            self.pre_syntax_tree.append(token)
        return self.pre_syntax_tree

    def build_head(self, contents):
        token = Head()
        token.type = self.types.TYPE_HEAD
        token.level = len(self.marker.RE_HEAD_LEVEL.search(contents).group())
        token.children = [contents[token.level+1:]]
        return token
    
    def build_code_block(self,contents: str):
        token = CodeBlock()
        listed_contents = contents.split("\n")
        token.language = listed_contents.pop(0)[3:]
        listed_contents.pop(-1)
        token.children = listed_contents
        return token
    
    def build_paragraph(self,contents):
        paragraph = Paragraph()
        paragraph.type = self.types.TYPE_PARAGRAPH
        match_iter = self.marker.RE_CONTEXT.finditer(contents)
        for match in match_iter:
            match_text = match.group()
            token = Text()
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
            token.contents = part.group(1)
            paragraph.children.append(token)
        return paragraph

    # def prebuild_paragraph(self):
    #     token = Token()
    #     token.type = "paragraph"
    #     raw_contents : list[str] = []
    #     while not self.marker.END_PARAGRAPH.match(self.tmp_syntax):
    #         raw_contents.append(self.tmp_syntax)
    #         self.tmp_syntax = self.converted_text.pop(0)
    #     else:
    #         token.contents = "\n".join(raw_contents)
    #     return token
    
    # def build_context(self, context):
    #     match_iter = self.marker.CONTEXT.finditer(context)
    #     syntax_tree : list[Token] = []
    #     for match in match_iter:
    #         match_text = match.group()
    #         if part:=re.match(self.marker.EMPHASIS,match_text):
    #             token = Token()
    #             token.type = "emphasis"
    #             token.contents = part.group(1)
    #             syntax_tree.append(token)
    #         elif part:=re.match(self.marker.ITALIC,match_text):
    #             token = Token()
    #             token.type = "italic"
    #             token.contents = part.group(1)
    #             syntax_tree.append(token)
    #         elif part:=re.match(self.marker.INLINE,match_text):
    #             token = Token()
    #             token.type = "inline"
    #             token.contents = part.group(1)
    #             syntax_tree.append(token)
    #         elif part:=re.match(self.marker.PLAINE,match_text):
    #             token = Token()
    #             token.type = "plain"
    #             token.contents = part.group(1)
    #             syntax_tree.append(token)
        
    #     return syntax_tree

    # def build_table(self,context : str):
    #     rows = context.split("\n")
    #     table = Table()
    #     table.header = [self.build_context(head) for head in filter(None, rows.pop(0).split("|"))]
    #     for pos in filter(None, rows.pop(0).split("|")):
    #         if self.marker.TABLE_LEFT.match(pos):
    #             table.position.append("left")
    #         elif self.marker.TABLLE_CENTER.match(pos):
    #             table.position.append("center")
    #         elif self.marker.TABLE_RIGHT.match(pos):
    #             table.position.append("right")
        
    #     for row in rows:
    #         table.cells.append([self.build_context(cell) for cell in filter(None, row.split("|"))])
        
    #     return table
    #     pass
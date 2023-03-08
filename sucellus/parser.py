from typing import Union
from typing import Any
from .token import Token
from .marker import Marker
from pathlib import Path

from sucellus import token

class Parser(object):
    read_text: str
    converted_text: list[str] = []
    pre_syntax_tree: list[Token] = []
    marker: Union[Marker, Any]
    tmp_syntax: str

    def __init__(self,marker = None):
        if marker:
            self.marker = marker
        else:
            self.marker = Marker()
    
    def read_file(self,file_path: str):
       self.read_text = Path(file_path).open().read()

    def convert_to_list(self):
        self.converted_text = self.read_text.split("\n")
    
    def pre_process(self):
        if self.converted_text[-1] != "":
            self.converted_text.append(r"")
        while self.converted_text:
            self.tmp_syntax = self.converted_text.pop(0)
            if self.marker.HEAD.match(self.tmp_syntax):
                token = self.build_head()
                self.pre_syntax_tree.append(token)
            elif self.marker.START_CODE_BLOCK.match(self.tmp_syntax):
                token = self.build_codeblock()
                self.pre_syntax_tree.append(token)
            elif self.marker.START_QUOTE_BLOCK.match(self.tmp_syntax):
                token = self.build_quote_block()
                self.pre_syntax_tree.append(token)
            elif self.marker.START_TABLE.match(self.tmp_syntax):
                token = self.build_table()
                self.pre_syntax_tree.append(token)
            else:
                token = self.build_paragraph()
                self.pre_syntax_tree.append(token)
        return self.pre_syntax_tree

    def build_head(self):
        token = Token()
        token.type = "head"
        token.contents = self.tmp_syntax
        return token
    
    def build_codeblock(self):
        token = Token()
        token.type = "code_block"
        raw_contents : list[str] = []
        while not self.marker.END_CODE_BLOCK.match(self.tmp_syntax):
            raw_contents.append(self.tmp_syntax)
            self.tmp_syntax = self.converted_text.pop(0)
        else:
            raw_contents.append(self.tmp_syntax)
            token.contents = "\n".join(raw_contents)
        return token

    def build_quote_block(self):
        token = Token()
        token.type = "quote_block"
        raw_contents: list[str] = []
        while not self.marker.END_QUOTE_BLOCK.match(self.tmp_syntax):
            raw_contents.append(self.tmp_syntax)
            self.tmp_syntax = self.converted_text.pop(0)
        else:
            token.contents = "\n".join(raw_contents)
        return token
    
    def build_table(self):
        token = Token()
        head_token = Token()
        position_token = Token()
        row_token = Token()
        token.type = "table"
        head_token.contents = self.tmp_syntax
        self.tmp_syntax = self.converted_text.pop(0)
        position_token.contents = self.tmp_syntax
        self.tmp_syntax =  self.converted_text.pop(0)
        raw_contents : list[str] = []
        while not self.marker.END_TABLE.match(self.tmp_syntax):
            raw_contents.append(self.tmp_syntax)
            self.tmp_syntax = self.converted_text.pop(0)
        else:
            row_token.contents = "\n".join(raw_contents)
        token.children += [head_token, position_token, row_token]
        return token
        
    def build_paragraph(self):
        token = Token()
        token.type = "paragraph"
        return token
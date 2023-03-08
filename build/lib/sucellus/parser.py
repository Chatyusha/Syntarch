from typing import Any
from .token import Token
from .marker import Marker
from pathlib import Path

class Parser(object):
    read_text: str
    converted_text: list[str] = []
    pre_syntax_tree: list[Token] = []
    marker: Any

    def __init__(self,marker = None):
        if marker:
            self.marker = marker
        else:
            self.marker = Marker()
    
    def read_file(self,file_path: str):
       self.read_text = Path(file_path).open().read()

    def convert_to_list(self):
        self.converted_text = self.read_text.split("\n\n")
    
    def pre_process(self):
        while self.converted_text:
            syntax = self.converted_text.pop(0)
            print("debug")
            if self.marker.HEAD.match(syntax):
                token = Token()
                token.type = "head"
                token.contents = syntax
                self.pre_syntax_tree.append(token)
            elif self.marker.START_CODE_BLOCK.match(syntax):
                token = Token()
                token.type = "code_block"
                while not self.marker.END_CODE_BLOCK.match(syntax):
                    token.children.append(syntax)
                    syntax = self.converted_text.pop(0)
                else:
                    token.children.append(syntax)
                self.pre_syntax_tree.append(token)
            else:
                token = Token()
                token.type = "paragraph"
                self.pre_syntax_tree.append(token)
        return self.pre_syntax_tree


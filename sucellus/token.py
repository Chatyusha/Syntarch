
from typing import Any


class Token():
    def toJSON(self):
        if self.children:
            return {
                "type" : self.type,
                "children":[i.toJSON() for i in self.children]
                }
        else:
            return {"type" : self.type, "contents" : self.contents}
    def __init__(self):
        self.type: str = ""
        self.contents : str = ""
        self.children = []

class Text(Token):
    def __init__(self):
        super().__init__()

class Head(Token):
    level:int
    def __init__(self):
        super().__init__()

class CodeBlock(Token):
    language : str
    def __init__(self):
        super().__init__()

class QuoteBlock(Token):
    def __init__(self):
        super().__init__()

class Paragraph(Token):
    def __init__(self):
        super().__init__()

class Table(Token):    
    def __init__(self):
        super().__init__()

class TableHead(Token):
    def __init__(self):
        super().__init__()

class TablePosition(Token):
    def __init__(self):
        super().__init__()

class TableRow(Token):
    def __init__(self):
        super().__init__()

class TableCell(Token):
    def __init__(self):
        super().__init__()

class DotList(Token):
    parent : Any
    items  = []
    def __init__(self):
        super().__init__()
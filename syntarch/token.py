
from typing import Any
from .types import TokenTypes


class Token():
    def toJSON(self):
        if self.children:
            return {
                "type" : self.type,
                "children":[i.toJSON() for i in self.children]
                }
        else:
            if self.type == TokenTypes.TYPE_HEAD:
                return {"type" : self.type, "level" : self.level, "contents" : self.contents}
            else:
                return {"type" : self.type, "contents" : self.contents}
    def __init__(self):
        self.type: str = ""
        self.level: int = 0
        self.contents : str = ""
        self.children = []

class DotList(Token):
    parent : Any
    items  = []
    def __init__(self):
        super().__init__()
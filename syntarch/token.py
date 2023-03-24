
from typing import Any
from .types import TokenTypes


class Token():
    def toJSON(self):
        token_object = {
                "type" : self.type,
                "level": self.level,
                "language": self.language,
                "contents":self.contents,
                "children":[i.toJSON() for i in self.children],
                "items":[i.toJSON() for i in self.items]
            }
        for key in list(token_object):
            if token_object[key] == None or token_object[key] == []:
                token_object.pop(key)
        return token_object
        # if self.children:
        #     return {
        #         "type" : self.type,
        #         "children":[i.toJSON() for i in self.children]
        #         }
        # else:
        #     if self.type == TokenTypes.TYPE_HEAD:
        #         return {"type" : self.type, "level" : self.level, "contents" : self.contents}
        #     else:
        #         return {"type" : self.type, "contents" : self.contents}
    def __init__(self):
        self.type: str = None
        self.contents : str = None
        self.level: int = None
        self.language: str = None
        self.children : list[Token] = []
        self.items : list[Token] = []
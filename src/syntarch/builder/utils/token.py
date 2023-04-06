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

    def __init__(self):
        self.type: str = None
        self.contents : str = None
        self.level: int = None
        self.language: str = None
        self.children : list[Token] = []
        self.items : list[Token] = []
        self.table_position : list[str] = []
        self.table_head : list[Token] = []
from .token import Token

class Codeblock(Token):
    def __init__(self):
        self.type = "Codeblock"
        self.language = ""

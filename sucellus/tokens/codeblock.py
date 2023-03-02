from .token import Token

class Codeblock(Token):
    def __init__(self):
        super().__init__()
        self.type = "Codeblock"
        self.language = ""

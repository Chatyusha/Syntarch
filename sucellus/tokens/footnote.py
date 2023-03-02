from .token import Token

class Footnote(Token):
    def __init__(self):
        self.type = "Footnote"
        self.marker = 0
        self.children = []

from .token import Token

class Quoteblock(Token):
    def __init__(self):
        self.type = "Quoteblock"
        self.children = []

from .token import Token

class Head(Token):
    def __init__(self):
        self.type = "Head"
        self.level = 0
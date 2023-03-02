from .token import Token

class Image(Token):
    def __init__(self):
        self.type = "Image"
        self.caption = ""
        self.path = ""

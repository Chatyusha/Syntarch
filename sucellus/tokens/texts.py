from .token import Token

class Text(Token):
    def __init__(self):
        self.type = "Text"
        self.children = []

class Plaintext(Text):
    def __init__(self):
        self.type = "Plaintext"

class Boldtext(Text):
    def __init__(self):
        self.type = "Boldtext"

class Italictext(Text):
    def __init__(self):
        self.type = "Italictext"

class Inlinecode(Text):
    def __init__(self):
        self.type = "Inlinecode"

class Inlinemath(Text):
    def __init__(self):
        self.type = "Inlinemath"

class Annotation(Text):
    def __init__(self):
        self.type = "Annotation"
        self.number = 0


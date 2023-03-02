from .token import Token

class List(Token):
    def __init__(self):
        self.type = "List"
        self.marker = "" # bullet/number
        self.children = []

class Item(List):
    def __init__(self):
       self.type = "Item" 
       self.level = 0
       self.children = []

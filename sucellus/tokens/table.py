from .token import Token

class Table(Token):
    def __init__(self):
        self.type = "Table"
        self.headers = []
        self.cell_positions = "" # e.g. "lcr" -> left/center/right
        self.children = [] # matrix of texts.Text

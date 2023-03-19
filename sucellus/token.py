
class Token():
    def help(self):
        print(
            """
            propaties
            ----------
            - type: type of context.
                - head : 
                - codeblock : 
                - quoteblock : 
                - paragraph : 
                - table
                    - table-head
                    - table-posision
                    - table-row
                - list
                - enumlist
            ----------
            """
        )

    def __init__(self):
        self.type: str
        self.contents: str
        self.children = []

class Head(Token):
    level:int
    def __init__(self):
        super().__init__()

class CodeBlock(Token):
    language : str
    def __init__(self):
        super().__init__()

class Paragraph(Token):
    def __init__(self):
        super().__init__()

class Table(Token):
    header: list[Token] = []
    position: list[str] = []
    cells: list[list[list[Token]]] = []

    def __init__(self):
        super().__init__()

class Text(Token):
    def __init__(self):
        super().__init__()
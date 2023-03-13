
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
        self.children: list[Token] = []
        self.level: int
        self.inline: str
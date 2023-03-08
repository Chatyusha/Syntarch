
class Token():
    def help(self):
        print(
            """
            propaties
            ----------
            - type: type of context, eg.) headline, paragraph, block
            """
        )

    def __init__(self):
        self.type: str
        self.contents: str
        self.children: list[Token] = []
        self.level: int
        self.inline: str

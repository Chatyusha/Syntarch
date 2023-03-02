import re

class Matchers():
    def __init__(self):
        self.MATCH_HEAD = re.compile(r"^#{1,6} ")
        self.MATCH_CODEBLOCK = re.compile(r"^```")
        self.MATCH_QUOATEBLOCK = re.compile(r"^> ")

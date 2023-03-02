from .tokens.headlines import Head
from .tokens.texts import Plaintext, Boldtext, Italictext, Inlinecode, Inlinemath
from .tokens.codeblock import Codeblock

from .matchers import Matchers

class Parser():
    def __init__(self,match_marker = None, builder = None):
        if not match_marker:
            self.__matches = Matchers()
        self.syntax_tree = [] 

    def readFile(self,path):
        with open(path) as textfile:
            self.__rawtext_iter = iter(textfile.read().split("\n")[:-1])

    def parse(self):
        for line in self.__rawtext_iter:
            if self.__matches.MATCH_CODEBLOCK.match(line):
                self.syntax_tree.append(self.build_codeblock(line))
            elif self.__matches.MATCH_HEAD.match(line):
                self.syntax_tree.append(self.build_head(line))
            else:
                pass

                    

    def build_head(self,line):
        head = Head()
        match = self.__matches.MATCH_HEAD.match(line)
        head.contents = [line[match.end():]]
        head.level = len(match.group())-1
        return head

    def build_codeblock(self,line):
        codeblock = Codeblock()
        print(vars(codeblock))
        codeblock.language = line[3:]
        next(self.__rawtext_iter) # 1行進む
        for code in self.__rawtext_iter:
            if self.__matches.MATCH_CODEBLOCK.match(code):
                break
            else:
                codeblock.contents.append(code)
        return codeblock
    
    def build_text(self,line):
        line_iter = iter(line)
        for character in line_iter:
            pass

    def text_analyze(self,line):
        pass

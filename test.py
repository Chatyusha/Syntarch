import unittest
from sucellus.parser import Parser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.md_parser = Parser()
        

if __name__ == "__main__":
    parser = Parser()
    file = "./tests/table.md"
    parser.read_file(file)
    # parser.convert_to_list()
    # parser.pre_process()
    # print(parser.pre_syntax_tree)
    a = parser.build_context("**hoge***fuga*`bar`hogehoge")
    exit(0)
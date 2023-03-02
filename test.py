import unittest
import json
import sucellus

from sucellus.parser import Parser

from sucellus.tokens import headlines, codeblock

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.md_parser = Parser()
    def test_head(self):
        input_texts = []
        expects = []
        input_filepath = "./tests/head/test.md"
        expects_jsonpath = "./tests/head/expect.json"
        self.md_parser.readFile(input_filepath)
        input_texts = self.md_parser._Parser__rawtext_iter
        with open(expects_jsonpath) as f:
            expects = json.load(f)

        results = [vars(self.md_parser.build_head(i)) for i in input_texts]
        for i,j in zip(expects,results):
            self.assertEqual(i,j)

    def test_codeblock(self):
        input_texts = []
        expects = []
        results = []
        input_filepath = "./tests/codeblock/test.md"
        self.md_parser.readFile(input_filepath)
        print(vars(self.md_parser.build_codeblock("```c++")))
        pass

    def test_text_analyze(self):
        line_text = r"abcde*efg***hij**\*kl*mn\o*p" 
        print(line_text)
        print(self.md_parser.text_analyze(line_text))
        



if __name__ == "__main__":
    unittest.main()

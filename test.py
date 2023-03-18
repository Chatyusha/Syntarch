from asyncore import read
from sucellus.parser import Parser

if __name__ == "__main__":
    parser = Parser()
    parser.read_file("./example.md")
    parser.pre_process()
    exit(0)
from syntarch.parser import Parser
import json
if __name__ == "__main__":
    parser = Parser()
    md_text = ""
    parser.read_file("./tests/example.ja.md")
    parser.build_markdown()
    path = "ast.json"
    with open(path,mode = "w") as f:
        md = []
        for i in parser.syntax_tree:
            md.append(i.toJSON())
        json.dump(md, f, indent=2, ensure_ascii=False)
    exit(0)
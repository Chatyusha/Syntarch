# Syntarch

Markdownで書かれたファイルを構文木に変換するPythonモジュールです。

## 使い方

### インストール方法

```sh
git clone https://github.com/Chatyusha/Syntarch.git
cd Syntarch
pip3 install .
```

```python
from syntarch.parser import Parser
import json

# jsonファイルに構文技を書き出すサンプル
if __name__ == "__main__":
    parser = Parser()
    file_path = "./tests/example.ja.md" # ここは手元の環境に合わせて
    json_path = "./syntax_tree.json"  # ここも手元の環境に合わせて
    parser.read_file(file_path)
    parser.build_markdown() 
    with open(path,mode = "w") as f:
        json.dump([i.toJSON() for i in parser.syntax_tree], f, indent=2, ensure_ascii=False)
```

## サポートしている構文

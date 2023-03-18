import re
from sucellus import marker

_marker = marker.Marker()

def test_table():
    table_text = "\n".join([
        "|abc|def|ghi|",
        "|:--|:-:|--:|",
        "|123|456|589|",
        "|1011|1213|1415|"
    ])
    print(table_text)
    T = re.compile(_marker.TABLE)
    t = T.search(table_text).group()

if __name__ == "__main__":
    test_table()
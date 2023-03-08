import re
class Marker():        
    START_CODE_BLOCK = re.compile(r"^```")
    END_CODE_BLOCK = re.compile(r"```$")
    START_QUOTE_BLOCK = re.compile(r"^> ")
    END_QUOTE_BLOCK = re.compile(r"^$")
    START_TABLE = re.compile(r"(\|.*)+\|$")
    END_TABLE = re.compile(r"^$")
    HEAD = re.compile(r"^#{1,6} ")
    ESCAPE = re.compile(r"^\\")
    START_BOLD = re.compile(r"^\*\*")
    START_ITARIC = re.compile(r"^\*")


    def __init__(self) -> None:
        pass

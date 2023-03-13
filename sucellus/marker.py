import re
class Marker():
    # Markers
    START_CODE_BLOCK = re.compile(r"^```")
    END_CODE_BLOCK = re.compile(r"```$")
    START_QUOTE_BLOCK = re.compile(r"^> ")
    END_QUOTE_BLOCK = re.compile(r"^$")
    START_TABLE = re.compile(r"(\|.*)+\|$")
    END_TABLE = re.compile(r"^$")
    END_PARAGRAPH = re.compile(r"^$")
    HEAD = re.compile(r"^#{1,6} ")

    # MatchPatterns
    EMPHASIS = r"\*([^*]+?)\*"
    ITALIC = r"\*\*([^*]+?)\*\*"
    INLINE = r"\`([^`]+?)\`"
    PLAINE = r"([^*`]+)"
    CONTEXT = re.compile(rf"{EMPHASIS}|{ITALIC}|{INLINE}|{PLAINE}")
    def __init__(self) -> None:
        pass

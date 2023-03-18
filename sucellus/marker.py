import re
class Marker(object):
    # Markers
    START_CODE_BLOCK = r"^```[^`]+$"
    END_CODE_BLOCK = r"^[^`]+```$"
    QUOTE_BLOCK = r"^(>(( [^>]*?)|)\n)*?> [^>]*?$"
    DISPLAY_MATH = r"^\$\$[^$]+?\$\$$"

    HEAD = r"^#{1,6} [^#]+?$"

    # MatchPatterns
    EMPHASIS = r"\*(((\\\*)|[^*])+?)\*"
    ITALIC = r"\*\*(((\\\*)|[^*])+?)\*\*"
    INLINE = r"`(((\\`)|[^`])+?)`"
    INLINE_MATH = r"\$(((\\\$)|[^$])+?)\$"
    PLAINE = r"(([^*`]|(\\\*)|(\`))+)"
    CONTEXT = rf"{EMPHASIS}|{ITALIC}|{INLINE}|{INLINE_MATH}|{PLAINE}"

    ## Table
    TABLE_LEFT = r"(:-+)"
    TABLE_CENTER = r"(:-+:)"
    TABLE_RIGHT = r"(-+:)"
    TABLE_POSITION = rf"((\|({TABLE_LEFT}|{TABLE_CENTER}|{TABLE_RIGHT}))+)\|"
    TABLE_CELL = r"([^|]+)"
    TABLE_ROW = rf"((\|{TABLE_CELL})+)\|"
    TABLE = rf"^{TABLE_ROW}\n{TABLE_POSITION}\n({TABLE_ROW}\n)*({TABLE_ROW})$"

    RE_HEAD = re.compile(HEAD)
    RE_START_CODE_BLOCK = re.compile(START_CODE_BLOCK)
    RE_END_CODE_BLOCK = re.compile(END_CODE_BLOCK)
    RE_QUOTE_BLOCK = re.compile(QUOTE_BLOCK)
    RE_DISPLAY_MATH = re.compile(DISPLAY_MATH)
    RE_TABLE = re.compile(TABLE)
    RE_CONTEXT = re.compile(CONTEXT)


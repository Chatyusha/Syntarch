import re
class Marker(object):
    # Markers
    CODE_BLOCK = r"^```[^`]+?```$"
    QUOTE_BLOCK = r"^(>(( [^>]*?)|)\n)*?> [^>]*?$"
    MATH_BLOCK = r"^\$\$[^$]+?\$\$$"

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

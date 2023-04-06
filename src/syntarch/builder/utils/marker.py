class Marker(object):
    CATEGORIES :dict = None

    # Category Separator
    CATEOGRY_SEPARATOR = "\n"

    ## Category
    CODE_BLOCK = r"^```"
    QUOTE = r"^>(| )"
    HEAD = r"^#{1,6} "
    DISPLAY_MATH = "^\$\$$"
    DOT_LIST = r"^( {4}|\t)*\*"
    TABLE = r"^(\|[^|]+)+\|"


    # Paragraph
    EMPTY_LINE = r"^$"
    ITALIC = r"\*(((\\\*)|[^*])+?)\*"
    EMPHASIS = r"\*\*(((\\\*)|[^*])+?)\*\*"
    INLINE = r"`(((\\`)|[^`])+?)`"
    INLINE_MATH = r"\$(((\\\$)|[^$])+?)\$"
    PLAINE = r"(([^*$`]|(\\\*)|(\\`)|(\\\$))+)"
    CONTEXT = rf"{EMPHASIS}|{ITALIC}|{INLINE}|{INLINE_MATH}|{PLAINE}"

    ## Table
    TABLE_LEFT = r"(:-+)"
    TABLE_CENTER = r"(:-+:)"
    TABLE_RIGHT = r"(-+:)"
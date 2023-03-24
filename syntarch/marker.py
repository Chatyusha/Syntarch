import re
from tkinter.font import ITALIC
class Marker(object):
    # Markers
    START_CODE_BLOCK = r"^```[^`]+$"
    END_CODE_BLOCK = r"^[^`]+```$"
    QUOTE_BLOCK = r"^(>(( [^>]*?)|)\n)*?> [^>]*?$"
    DISPLAY_MATH = r"^\$\$[^$]+?\$\$$"
    HEAD = r"^#{1,6} "
    DOT_LIST = r"^( {4}|\t)*\* .*$"

    # MatchPatterns
    NEW_LINE = r"^$"
    ITALIC = r"\*(((\\\*)|[^*])+?)\*"
    EMPHASIS = r"\*\*(((\\\*)|[^*])+?)\*\*"
    INLINE = r"`(((\\`)|[^`])+?)`"
    INLINE_MATH = r"\$(((\\\$)|[^$])+?)\$"
    PLAINE = r"(([^*$`]|(\\\*)|(\`)|(\\\$))+)"
    CONTEXT = rf"{EMPHASIS}|{ITALIC}|{INLINE}|{INLINE_MATH}|{PLAINE}"

    ## CodeBlock
    CODE_BLOCK_MARK = r"^```"

    ## Table
    TABLE_LEFT = r"(:-+)"
    TABLE_CENTER = r"(:-+:)"
    TABLE_RIGHT = r"(-+:)"
    TABLE_POSITION = rf"((\|({TABLE_LEFT}|{TABLE_CENTER}|{TABLE_RIGHT}))+)\|"
    TABLE_CELL = r"([^|]+)"
    TABLE_ROW = rf"((\|{TABLE_CELL})+)\|"
    TABLE = rf"^{TABLE_ROW}\n{TABLE_POSITION}\n({TABLE_ROW}\n)*({TABLE_ROW})$"

    ## HEAD
    HEAD_LEVEL = r"^#{1,6}"

    ## QUOTE
    NOT_EMPTY_QUOTE_LINE = r"(^$>)|(^> )"
    EMPTY_QUOTE_LINE = r"(^>$)"
    QUOTE_LINE = rf"{NOT_EMPTY_QUOTE_LINE}|{EMPTY_QUOTE_LINE}"

    ## DOT_LIST
    DOT_LIST_INDENT = r"^( {2}|\t)"
    DOT_LIST_MARKER = r"^\* "

    RE_HEAD = re.compile(HEAD)
    RE_START_CODE_BLOCK = re.compile(START_CODE_BLOCK)
    RE_END_CODE_BLOCK = re.compile(END_CODE_BLOCK)
    RE_QUOTE_BLOCK = re.compile(QUOTE_BLOCK)
    RE_DISPLAY_MATH = re.compile(DISPLAY_MATH)
    RE_TABLE = re.compile(TABLE)
    RE_DOT_LIST = re.compile(DOT_LIST,re.MULTILINE)
    RE_CONTEXT = re.compile(CONTEXT)

    RE_CODE_BLOCK_MARK = re.compile(CODE_BLOCK_MARK,re.MULTILINE)

    RE_TABLE_POSITION_LEFT = re.compile(TABLE_LEFT)
    RE_TABLE_POSITION_CENTER = re.compile(TABLE_CENTER)
    RE_TABLE_POSITION_RIGHT = re.compile(TABLE_RIGHT)

    RE_HEAD_LEVEL = re.compile(HEAD_LEVEL)
    RE_QUOTE_LINE = re.compile(QUOTE_LINE,re.MULTILINE)

    RE_DOT_LIST_INDENT = re.compile(DOT_LIST_INDENT)
    RE_DOT_LIST_MARKER = re.compile(DOT_LIST_MARKER)

    RE_EMPHASIS = re.compile(EMPHASIS)
    RE_NEW_LINE = re.compile(NEW_LINE)
    RE_ITALIC = re.compile(ITALIC)
    RE_INLINE = re.compile(INLINE)
    RE_INLINE_MATH = re.compile(INLINE_MATH)
    RE_PLAINE = re.compile(PLAINE)
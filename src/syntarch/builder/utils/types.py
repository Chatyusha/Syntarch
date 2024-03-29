class TokenTypes():
    TYPE_HEAD = "head"
    TYPE_CODE_BLOCK = "code_block"
    TYPE_QUOTE = "quote"
    TYPE_TABLE = "table"
    TYPE_PARAGRAPH = "paragraph"
    TYPE_DISPLAY_MATH = "display_math"
    TYPE_DOT_LIST = "dot_list"
    TYPE_PLAINE = "plaine"
    TYPE_EMPHASIS = "emphasis"
    TYPE_ITALIC = "italic"
    TYPE_INLINE = "inline"
    TYPE_INLINE_MATH = "inline_math"
    TYPE_NEW_LINE = "new_line"
    TYPE_PHRASE = "phrase"

    TYPE_TABLE_ROW = "table_row"
    TYPE_TABLE_CELL = "table_cell"
    TYPE_TABLE_POSITIONS = "table_positions"
    TYPE_TABLE_POSITION = "table_position"
    TABLE_POSITION_LEFT = "table_left"
    TABLE_POSITION_CENTER = "table_center"
    TABLE_POSITION_RIGHT = "table_right"

    def __init__(self):
        pass

class TokenValues():
    CONST_TABLE_POSITION_LEFT = "left"
    CONST_TABLE_POSITION_CENTER = "center"
    CONST_TABLE_POSITION_RIGHT = "right"
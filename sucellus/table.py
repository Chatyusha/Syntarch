from turtle import position
from .token import Token


class Table(Token):
    header: list[Token] = []
    position: list[str] = []
    cells: list[list[list[Token]]] = []

    def __init__(self):
        super().__init__()
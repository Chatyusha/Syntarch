from collections import deque
from typing import Union
from types import FunctionType
import re
from .utils import marker
from .utils import matcher
from .utils import token
from .utils import types

class PreBuilder(object):
    __marker : marker.Marker = None
    __matcher : matcher.Matcher = None
    __types : types.TokenTypes = None
    CATEGORY_SEPARATOR: str
    __CATEGORIES_MAP : list[dict[str, Union[re.Pattern,FunctionType]]] = []
    __separated_text : list[str] = []
    __line_contents: list[dict[str,str]] = []
    __presyntax_tree : list[token.Token] = []
    __index : int = 0


    def __init__(self, marker : marker.Marker):
        self.__marker = marker
        self.__matcher = matcher.Matcher(self.__marker)
        self.CATEGORY_SEPARATOR = self.__marker.CATEOGRY_SEPARATOR
        self.__CATEGORIES_MAP = [
            {
                "type" : types.TokenTypes.TYPE_HEAD,
                "pattern": self.__matcher.RE_HEAD,
                "builder" : self.prebuild_head
            },
            {
                "type" : types.TokenTypes.TYPE_QUOTE,
                "pattern" : self.__matcher.RE_QUOTE,
                "builder" : self.prebuild_quote
            },
            {
                "type" : types.TokenTypes.TYPE_DOT_LIST,
                "pattern" : self.__matcher.RE_DOTLIST,
                "builder" : self.prebuild_dotlist
            }
        ]
    
    def __separate(self,raw_text : str):
        self.__separated_text = deque(raw_text.split(self.CATEGORY_SEPARATOR))

    # 一行ずつの要素解析
    def liner_build(self,raw_text : str):
        # SEPARATORを区切り文字として分割
        self.__separate(raw_text)

        for contents in self.__separated_text:
            for category in self.__CATEGORIES_MAP:
                # Categotyのどれかにマッチ
                if category["pattern"].match(contents):
                    self.__line_contents.append(
                        {
                            "type":category["type"],
                            "contents":contents
                        }
                    )
                    break
            # カテゴリーのどれにもマッチしない
            else:
                self.__line_contents.append(
                    {
                        "type" : types.TokenTypes.TYPE_PARAGRAPH,
                        "contents" : contents
                    }
                )

    def pre_build(self):
        for fragment in self.__line_contents:
            for pre_type in self.__CATEGORIES_MAP:
                if fragment["type"] == pre_type["type"]:
                    pre_type["builder"]()

    def prebuild_head(self):
        _token = token.Token()
        _token.type = types.TokenTypes.TYPE_HEAD
        _token.contents = self.__line_contents[self.__index]
        self.__presyntax_tree.append(_token)
        self.__index_update()
        print("called prebuild_head")

    def prebuild_quote(self,):
        _token  = token.Token()
        _token.type = types.TokenTypes.TYPE_QUOTE
        _list_contents = []
        while (fragment:=self.__line_contents[self.__index])["type"] == types.TokenTypes.TYPE_QUOTE: 
            _list_contents.append(fragment["contents"])
            self.__index_update()
        _token.contents = "\n".join(_list_contents)
        self.__presyntax_tree.append(_token)

    def prebuild_dotlist(self):
        _token = token.Token()
        _token.type = types.TokenTypes.TYPE_DOT_LIST
        _list_contents = []
        while (fragment:=self.__line_contents[self.__index])["type"] == types.TokenTypes.TYPE_DOT_LIST: 
            _list_contents.append(fragment["contents"])
            self.__index_update()
        _token.contents = "\n".join(_list_contents)
        self.__presyntax_tree.append(_token)
        print("called prebuild_dotlist")
    

    def __index_update(self):
        self.__index += 1
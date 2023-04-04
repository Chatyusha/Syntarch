from typing import Union
import re
from .utils import marker
from .utils import matcher
from .utils import token
from .utils import types

class PreBuilder(object):
    _marker : marker.Marker = None
    _matcher : matcher.Matcher = None
    _CATEGORIES_PAIR : list[dict[str, Union[re.Pattern, None]]] = []
    _presyntax_tree = list[token.Token]

    def __init__(self, marker : marker.Marker):
        self._marker = marker
        self._matcher = matcher.Matcher(self._marker)
        self._CATEGORIES_PAIR = [
            {
                "pattern": self._matcher.RE_HEAD,
                "builder" : self.prebuild_head
            },
            {
                "pattern" : self._matcher.RE_QUOTE,
                "builder" : self.prebuild_quote
            },
            {
                "pattern" : self._matcher.RE_DOTLIST,
                "builder" : self.prebuild_dotlist
            }
        ]

    def prebuild(self,raw_text : str):
        list_raw_text = raw_text.split(self.CATEGORY_SEPARATOR)
        for _line in list_raw_text:
            for category in self._CATEGORIES_PAIR:
                if category["pattern"].match(_line):
                    category["builder"](_line)
                    break

    def prebuild_head(self,raw_line):
        _token = token.Token()
        _token.type = types.TokenTypes.TYPE_HEAD
        _token.contents = raw_line
        return _token

    def prebuild_quote(self,raw_line):
        print("called prebuild_quote")  

    def prebuild_dotlist(self,raw_line):
        print("called prebuild_dotlist")
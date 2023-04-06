from . import marker
import re

class Matcher(object):
    _marker : marker.Marker = None

    RE_HEAD = None
    RE_QUOTE = None
    RE_DOTLIST = None
    RE_TABLE = None
    RE_CODE_BLOCK = None
    RE_DISPLAY_MATH = None

    def __init__(self,_marker : marker.Marker):
        self._marker = _marker
        self.RE_HEAD = re.compile(_marker.HEAD,re.MULTILINE)
        self.RE_QUOTE = re.compile(_marker.QUOTE,re.MULTILINE)
        self.RE_DOTLIST = re.compile(_marker.DOT_LIST,re.MULTILINE)
        self.RE_TABLE = re.compile(_marker.TABLE,re.MULTILINE)
        self.RE_CODE_BLOCK = re.compile(_marker.CODE_BLOCK,re.MULTILINE)
        self.RE_DISPLAY_MATH = re.compile(_marker.DISPLAY_MATH,re.MULTILINE)
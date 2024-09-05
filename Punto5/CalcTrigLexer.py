# Generated from CalcTrig.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,43,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,5,4,5,33,8,5,11,5,12,5,34,1,6,4,6,38,8,6,11,6,12,6,39,1,
        6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,3,0,9,
        10,13,13,32,32,44,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,
        0,5,19,1,0,0,0,7,23,1,0,0,0,9,27,1,0,0,0,11,32,1,0,0,0,13,37,1,0,
        0,0,15,16,5,40,0,0,16,2,1,0,0,0,17,18,5,41,0,0,18,4,1,0,0,0,19,20,
        5,115,0,0,20,21,5,105,0,0,21,22,5,110,0,0,22,6,1,0,0,0,23,24,5,99,
        0,0,24,25,5,111,0,0,25,26,5,115,0,0,26,8,1,0,0,0,27,28,5,116,0,0,
        28,29,5,97,0,0,29,30,5,110,0,0,30,10,1,0,0,0,31,33,7,0,0,0,32,31,
        1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,12,1,0,0,0,
        36,38,7,1,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,41,1,0,0,0,41,42,6,6,0,0,42,14,1,0,0,0,3,0,34,39,1,6,0,
        0
    ]

class CalcTrigLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SIN = 3
    COS = 4
    TAN = 5
    INT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'sin'", "'cos'", "'tan'" ]

    symbolicNames = [ "<INVALID>",
            "SIN", "COS", "TAN", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "SIN", "COS", "TAN", "INT", "WS" ]

    grammarFileName = "CalcTrig.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



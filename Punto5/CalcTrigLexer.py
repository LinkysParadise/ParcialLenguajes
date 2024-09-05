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
        4,0,7,55,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,4,2,21,8,2,11,2,12,2,22,1,3,4,3,26,8,3,
        11,3,12,3,27,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,38,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,3,5,46,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,54,8,6,0,
        0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,2,1,0,48,57,3,0,9,10,13,13,
        32,32,59,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,20,1,0,
        0,0,7,25,1,0,0,0,9,37,1,0,0,0,11,45,1,0,0,0,13,53,1,0,0,0,15,16,
        5,40,0,0,16,2,1,0,0,0,17,18,5,41,0,0,18,4,1,0,0,0,19,21,7,0,0,0,
        20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,6,1,0,
        0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,29,1,0,0,0,29,30,6,3,0,0,30,8,1,0,0,0,31,32,5,115,0,0,
        32,33,5,105,0,0,33,38,5,110,0,0,34,35,5,83,0,0,35,36,5,105,0,0,36,
        38,5,110,0,0,37,31,1,0,0,0,37,34,1,0,0,0,38,10,1,0,0,0,39,40,5,99,
        0,0,40,41,5,111,0,0,41,46,5,115,0,0,42,43,5,67,0,0,43,44,5,111,0,
        0,44,46,5,115,0,0,45,39,1,0,0,0,45,42,1,0,0,0,46,12,1,0,0,0,47,48,
        5,116,0,0,48,49,5,97,0,0,49,54,5,110,0,0,50,51,5,84,0,0,51,52,5,
        97,0,0,52,54,5,110,0,0,53,47,1,0,0,0,53,50,1,0,0,0,54,14,1,0,0,0,
        6,0,22,27,37,45,53,1,6,0,0
    ]

class CalcTrigLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INT = 3
    WS = 4
    SIN = 5
    COS = 6
    TAN = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS", "SIN", "COS", "TAN" ]

    ruleNames = [ "T__0", "T__1", "INT", "WS", "SIN", "COS", "TAN" ]

    grammarFileName = "CalcTrig.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



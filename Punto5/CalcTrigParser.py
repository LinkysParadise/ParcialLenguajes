# Generated from CalcTrig.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,33,0,9,1,0,0,0,
        2,13,1,0,0,0,4,30,1,0,0,0,6,32,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,
        10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,
        2,0,14,3,1,0,0,0,15,16,5,3,0,0,16,17,5,1,0,0,17,18,3,6,3,0,18,19,
        5,2,0,0,19,31,1,0,0,0,20,21,5,4,0,0,21,22,5,1,0,0,22,23,3,6,3,0,
        23,24,5,2,0,0,24,31,1,0,0,0,25,26,5,5,0,0,26,27,5,1,0,0,27,28,3,
        6,3,0,28,29,5,2,0,0,29,31,1,0,0,0,30,15,1,0,0,0,30,20,1,0,0,0,30,
        25,1,0,0,0,31,5,1,0,0,0,32,33,5,6,0,0,33,7,1,0,0,0,2,11,30
    ]

class CalcTrigParser ( Parser ):

    grammarFileName = "CalcTrig.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'sin'", "'cos'", "'tan'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SIN", "COS", 
                      "TAN", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_function = 2
    RULE_num = 3

    ruleNames =  [ "prog", "stat", "function", "num" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SIN=3
    COS=4
    TAN=5
    INT=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcTrigParser.StatContext)
            else:
                return self.getTypedRuleContext(CalcTrigParser.StatContext,i)


        def getRuleIndex(self):
            return CalcTrigParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalcTrigParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcTrigParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(CalcTrigParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = CalcTrigParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            localctx = CalcTrigParser.PrintExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcTrigParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CosFunctionContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(CalcTrigParser.COS, 0)
        def num(self):
            return self.getTypedRuleContext(CalcTrigParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunction" ):
                listener.enterCosFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunction" ):
                listener.exitCosFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunction" ):
                return visitor.visitCosFunction(self)
            else:
                return visitor.visitChildren(self)


    class SinFunctionContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(CalcTrigParser.SIN, 0)
        def num(self):
            return self.getTypedRuleContext(CalcTrigParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFunction" ):
                listener.enterSinFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFunction" ):
                listener.exitSinFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunction" ):
                return visitor.visitSinFunction(self)
            else:
                return visitor.visitChildren(self)


    class TanFunctionContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(CalcTrigParser.TAN, 0)
        def num(self):
            return self.getTypedRuleContext(CalcTrigParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunction" ):
                listener.enterTanFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunction" ):
                listener.exitTanFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunction" ):
                return visitor.visitTanFunction(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = CalcTrigParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = CalcTrigParser.SinFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(CalcTrigParser.SIN)
                self.state = 16
                self.match(CalcTrigParser.T__0)
                self.state = 17
                self.num()
                self.state = 18
                self.match(CalcTrigParser.T__1)
                pass
            elif token in [4]:
                localctx = CalcTrigParser.CosFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(CalcTrigParser.COS)
                self.state = 21
                self.match(CalcTrigParser.T__0)
                self.state = 22
                self.num()
                self.state = 23
                self.match(CalcTrigParser.T__1)
                pass
            elif token in [5]:
                localctx = CalcTrigParser.TanFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(CalcTrigParser.TAN)
                self.state = 26
                self.match(CalcTrigParser.T__0)
                self.state = 27
                self.num()
                self.state = 28
                self.match(CalcTrigParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcTrigParser.RULE_num

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalcTrigParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def num(self):

        localctx = CalcTrigParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_num)
        try:
            localctx = CalcTrigParser.IntContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(CalcTrigParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        4,1,7,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,30,8,2,1,2,0,0,3,0,2,4,0,0,32,0,7,1,0,0,0,2,11,1,0,0,0,4,29,
        1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,
        0,0,10,1,1,0,0,0,11,12,3,4,2,0,12,3,1,0,0,0,13,14,5,5,0,0,14,15,
        5,1,0,0,15,16,3,4,2,0,16,17,5,2,0,0,17,30,1,0,0,0,18,19,5,6,0,0,
        19,20,5,1,0,0,20,21,3,4,2,0,21,22,5,2,0,0,22,30,1,0,0,0,23,24,5,
        7,0,0,24,25,5,1,0,0,25,26,3,4,2,0,26,27,5,2,0,0,27,30,1,0,0,0,28,
        30,5,3,0,0,29,13,1,0,0,0,29,18,1,0,0,0,29,23,1,0,0,0,29,28,1,0,0,
        0,30,5,1,0,0,0,2,9,29
    ]

class CalcTrigParser ( Parser ):

    grammarFileName = "CalcTrig.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "'sin'", "'cos'", "'tan'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT", "WS", 
                      "SIN", "COS", "TAN" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    WS=4
    SIN=5
    COS=6
    TAN=7

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 232) != 0)):
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

        def expr(self):
            return self.getTypedRuleContext(CalcTrigParser.ExprContext,0)


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
            self.state = 11
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcTrigParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CosFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(CalcTrigParser.COS, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcTrigParser.ExprContext,0)


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


    class SinFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(CalcTrigParser.SIN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcTrigParser.ExprContext,0)


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


    class TanFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(CalcTrigParser.TAN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcTrigParser.ExprContext,0)


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


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcTrigParser.ExprContext
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



    def expr(self):

        localctx = CalcTrigParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = CalcTrigParser.SinFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(CalcTrigParser.SIN)
                self.state = 14
                self.match(CalcTrigParser.T__0)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(CalcTrigParser.T__1)
                pass
            elif token in [6]:
                localctx = CalcTrigParser.CosFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(CalcTrigParser.COS)
                self.state = 19
                self.match(CalcTrigParser.T__0)
                self.state = 20
                self.expr()
                self.state = 21
                self.match(CalcTrigParser.T__1)
                pass
            elif token in [7]:
                localctx = CalcTrigParser.TanFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(CalcTrigParser.TAN)
                self.state = 24
                self.match(CalcTrigParser.T__0)
                self.state = 25
                self.expr()
                self.state = 26
                self.match(CalcTrigParser.T__1)
                pass
            elif token in [3]:
                localctx = CalcTrigParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(CalcTrigParser.INT)
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






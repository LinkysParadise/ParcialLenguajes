# Generated from CalcTrig.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcTrigParser import CalcTrigParser
else:
    from CalcTrigParser import CalcTrigParser

# This class defines a complete listener for a parse tree produced by CalcTrigParser.
class CalcTrigListener(ParseTreeListener):

    # Enter a parse tree produced by CalcTrigParser#prog.
    def enterProg(self, ctx:CalcTrigParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#prog.
    def exitProg(self, ctx:CalcTrigParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcTrigParser#printExpr.
    def enterPrintExpr(self, ctx:CalcTrigParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#printExpr.
    def exitPrintExpr(self, ctx:CalcTrigParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalcTrigParser#SinFunction.
    def enterSinFunction(self, ctx:CalcTrigParser.SinFunctionContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#SinFunction.
    def exitSinFunction(self, ctx:CalcTrigParser.SinFunctionContext):
        pass


    # Enter a parse tree produced by CalcTrigParser#CosFunction.
    def enterCosFunction(self, ctx:CalcTrigParser.CosFunctionContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#CosFunction.
    def exitCosFunction(self, ctx:CalcTrigParser.CosFunctionContext):
        pass


    # Enter a parse tree produced by CalcTrigParser#TanFunction.
    def enterTanFunction(self, ctx:CalcTrigParser.TanFunctionContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#TanFunction.
    def exitTanFunction(self, ctx:CalcTrigParser.TanFunctionContext):
        pass


    # Enter a parse tree produced by CalcTrigParser#int.
    def enterInt(self, ctx:CalcTrigParser.IntContext):
        pass

    # Exit a parse tree produced by CalcTrigParser#int.
    def exitInt(self, ctx:CalcTrigParser.IntContext):
        pass



del CalcTrigParser
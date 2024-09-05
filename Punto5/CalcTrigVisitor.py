# Generated from CalcTrig.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcTrigParser import CalcTrigParser
else:
    from CalcTrigParser import CalcTrigParser

# This class defines a complete generic visitor for a parse tree produced by CalcTrigParser.

class CalcTrigVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcTrigParser#prog.
    def visitProg(self, ctx:CalcTrigParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcTrigParser#printExpr.
    def visitPrintExpr(self, ctx:CalcTrigParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcTrigParser#SinFunction.
    def visitSinFunction(self, ctx:CalcTrigParser.SinFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcTrigParser#CosFunction.
    def visitCosFunction(self, ctx:CalcTrigParser.CosFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcTrigParser#TanFunction.
    def visitTanFunction(self, ctx:CalcTrigParser.TanFunctionContext):
        return self.visitChildren(ctx)



del CalcTrigParser
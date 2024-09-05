from CalcTrigVisitor import CalcTrigVisitor
from CalcTrigParser import CalcTrigParser
from antlr4 import *
from antlr4.InputStream import InputStream
import math


class MyVisitor(CalcTrigVisitor):

    def visitPrintExpr(self, ctx: CalcTrigParser.PrintExprContext):
        value = self.visit(ctx.function())
        print(value)
        return value
    
    def visitSinFunction(self, ctx: CalcTrigParser.SinFunctionContext):
        return math.sin(math.radians(self.visit(ctx.expr())))

    def visitCosFunction(self, ctx: CalcTrigParser.CosFunctionContext):
        return math.cos(math.radians(self.visit(ctx.expr())))

    def visitTanFunction(self, ctx: CalcTrigParser.TanFunctionContext):
        return math.tan(math.radians(self.visit(ctx.expr())))


def main():
    import sys
    import antlr4
    from antlr4.InputStream import InputStream
    from CalcTrigLexer import CalcTrigLexer
    from CalcTrigParser import CalcTrigParser

    if len(sys.argv) != 2:
        print("Usage: python CalcTrigVisitor.py <expression>")
        return

    expression = sys.argv[1]
    input_stream = InputStream(expression)
    lexer = CalcTrigLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcTrigParser(stream)
    tree = parser.prog()

    visitor = MyVisitor()
    result = visitor.visit(tree)
    print("Result:", result)

if __name__ == '__main__':
    main()
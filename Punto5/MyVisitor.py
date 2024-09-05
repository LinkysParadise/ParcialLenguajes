from CalcTrigVisitor import CalcTrigVisitor
from CalcTrigParser import CalcTrigParser
from CalcTrigLexer import  CalcTrigLexer
from antlr4 import *
import math
import sys

class MyVisitor(CalcTrigVisitor):
    
    def visitPrintExpr(self, ctx: CalcTrigParser.PrintExprContext):
        return self.visit(ctx.expr())

    def visitSinFunction(self, ctx: CalcTrigParser.SinFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in SinFunction")
        return math.sin(math.radians(value))

    def visitCosFunction(self, ctx: CalcTrigParser.CosFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in CosFunction")
        return math.cos(math.radians(value))

    def visitTanFunction(self, ctx: CalcTrigParser.TanFunctionContext):
        value = self.visit(ctx.expr())
        if value is None:
            raise ValueError("Expected numeric value in TanFunction")
        return math.tan(math.radians(value))

    def visitInt(self, ctx: CalcTrigParser.IntContext):
        return int(ctx.getText())

def process_line(line, visitor):
    input_stream = InputStream(line)
    lexer = CalcTrigLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcTrigParser(token_stream)
    tree = parser.stat() 
    result = visitor.visit(tree)

    if result is not None:
        print("Result: ", result)

if __name__ == '__main__':
    visitor = MyVisitor()

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                process_line(line.strip(), visitor)
    else:
        while True:
            try:
                line = input(">> ")
                if line.strip() == "":
                    break
                process_line(line, visitor)
            except EOFError:
                break

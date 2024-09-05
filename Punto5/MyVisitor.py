from CalcTrigVisitor import CalcTrigVisitor
from CalcTrigParser import CalcTrigParser
from antlr4 import *
import math

class MyVisitor(CalcTrigVisitor):
    
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

def main():
    import sys
    from antlr4 import InputStream
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
    try:
        result = visitor.visit(tree)
        print("Result:", result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

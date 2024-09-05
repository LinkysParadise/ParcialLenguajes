from antlr4 import *
from MyVisitor import MyVisitor
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
    result = visitor.visit(tree)
    print("Result:", result)

if __name__ == '__main__':
    main()

import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def code(source):
    lexer = Lexer(source)
    tokens = lexer.lex()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(ast)

def main():
    if len(sys.argv) < 2:
        print("Usage: L <source_file>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            source_code = f.read()
        code(source_code)
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == '__main__':
    main()

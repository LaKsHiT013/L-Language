import os
import sys

if getattr(sys, 'frozen', False):
    # If bundled by PyInstaller, use the directory of the executable.
    current_dir = os.path.dirname(sys.executable)
else:
    # Otherwise, use the parent directory of the Compile folder.
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Ensure the parent directory (that contains the 'Compile' package) is in sys.path.
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from Compile.lexer import Lexer
from Compile.parser import Parser
from Compile.interpreter import Interpreter

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

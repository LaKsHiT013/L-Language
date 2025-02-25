import re

class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value}, line={self.line}, col={self.column})"

token_specs = [
    (r'^\s+', None),
    (r'^//.*', None),
    (r'^Shuru\s+Krte\s+Hai\b', 'PROGRAM_START'),
    (r'^Ab\s+Thak\s+gaya\b', 'PROGRAM_END'),
    (r'^maan\s+le\b', 'VAR_DECL'),
    (r'^likh\s+bey\b', 'PRINT'),
    (r'^bhai\s+agar\b', 'IF'),
    (r'^nahi\s+to\s+bhai\b', 'ELSE_IF'),
    (r'^warna\s+last\s+option\b', 'ELSE'),
    (r'^jab\s+tak\b', 'WHILE'),
    (r'^bahar\s+nikal\s+ja\b', 'BREAK'),
    (r'^chal\s+aage\s+badh\b', 'CONTINUE'),
    (r'^==', 'EQUALS'),
    (r'^!=', 'NOT_EQUALS'),
    (r'^<=', 'LESS_EQUAL'),
    (r'^>=', 'GREATER_EQUAL'),
    (r'^<', 'LESS'),
    (r'^>', 'GREATER'),
    (r'^\+=', 'PLUS_EQUAL'),
    (r'^-=', 'MINUS_EQUAL'),
    (r'^\*=', 'MULTIPLY_EQUAL'),
    (r'^/=', 'DIVIDE_EQUAL'),
    (r'^\+', 'PLUS'),
    (r'^\-', 'MINUS'),
    (r'^\*', 'MULTIPLY'),
    (r'^/', 'DIVIDE'),
    (r'^=', 'ASSIGN'),
    (r'^\(', 'LPAREN'),
    (r'^\)', 'RPAREN'),
    (r'^\{', 'LBRACE'),
    (r'^\}', 'RBRACE'),
    (r'^;', 'SEMICOLON'),
    (r'^,', 'COMMA'),
    (r'^\d+(\.\d+)?', 'NUMBER'),
    (r'^"([^"\\]|\\.)*"', 'STRING'),
    (r"^'([^'\\]|\\.)*'", 'STRING'),
    (r'^\bnalla\b', 'NULL'),
    (r'^\bSahi\b', 'BOOLEAN'),
    (r'^\bGalat\b', 'BOOLEAN'),
    (r'^[A-Za-z_][A-Za-z0-9_]*', 'IDENTIFIER'),
]
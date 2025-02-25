import re
from tokens import Token, token_specs

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def lex(self):
        while self.pos < len(self.text):
            match_found = False
            substring = self.text[self.pos:]
            for pattern, token_type in token_specs:
                regex = re.compile(pattern)
                match = regex.match(substring)
                if match:
                    match_found = True
                    text_value = match.group(0)
                    if token_type:
                        value = text_value
                        if token_type == 'NUMBER':
                            value = float(text_value) if '.' in text_value else int(text_value)
                        elif token_type == 'STRING':
                            value = text_value[1:-1]
                        elif token_type == 'BOOLEAN':
                            value = True if text_value.strip() == 'sahi' else False
                        elif token_type == 'NULL':
                            value = None
                        self.tokens.append(Token(token_type, value, self.line, self.column))
                    self.update_position(text_value)
                    break
            if not match_found:
                raise Exception(f"Unexpected token at line {self.line}, column {self.column}")
        self.tokens.append(Token('EOF', None, self.line, self.column))
        return self.tokens

    def update_position(self, text_value):
        lines = text_value.split('\n')
        if len(lines) > 1:
            self.line += len(lines) - 1
            self.column = len(lines[-1]) + 1
        else:
            self.column += len(text_value)
        self.pos += len(text_value)

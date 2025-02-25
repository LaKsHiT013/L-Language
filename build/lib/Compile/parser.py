from tokens import Token
from ast_nodes import *

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0


    def current_token(self):
        return self.tokens[self.pos]


    def eat(self, token_type):
        token = self.current_token()
        if token.type == token_type:
            self.pos += 1
            return token
        else:
            raise Exception(f"Expected token {token_type} but got {token.type} at line {token.line}, column {token.column}")


    def parse(self):
        self.eat('PROGRAM_START')
        statements = self.parse_statements()
        self.eat('PROGRAM_END')
        return Program(statements)


    def parse_statements(self):
        statements = []
        while self.current_token().type not in ['PROGRAM_END', 'EOF', 'RBRACE']:
            statements.append(self.parse_statement())
        return statements


    def parse_statement(self):
        
        token = self.current_token()
        
        if token.type == 'VAR_DECL':
            return self.parse_var_decl()
        
        elif token.type == 'PRINT':
            return self.parse_print()
        
        elif token.type == 'IF':
            return self.parse_if()
        elif token.type == 'WHILE':
            return self.parse_while()
        
        elif token.type == 'BREAK':
            self.eat('BREAK')
            self.eat('SEMICOLON')
            return Break()
        
        elif token.type == 'CONTINUE':
            self.eat('CONTINUE')
            self.eat('SEMICOLON')
            return Continue()
        
        elif token.type == 'LBRACE':
            return self.parse_block()
        
        else:
            if token.type == 'IDENTIFIER':
                next_token = self.tokens[self.pos+1] if self.pos+1 < len(self.tokens) else None
                if next_token and (next_token.type == 'ASSIGN' or next_token.type in ['PLUS_EQUAL', 'MINUS_EQUAL', 'MULTIPLY_EQUAL', 'DIVIDE_EQUAL']):
                    return self.parse_assignment()

            expr = self.parse_expression()
            self.eat('SEMICOLON')
            return expr


    def parse_block(self):
        self.eat('LBRACE')
        statements = self.parse_statements()
        self.eat('RBRACE')
        return Block(statements)


    def parse_var_decl(self):
        self.eat('VAR_DECL')
        identifier = self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        initializer = self.parse_expression()
        self.eat('SEMICOLON')
        return VarDecl(identifier.value, initializer)


    def parse_assignment(self):
        identifier = self.eat('IDENTIFIER')
        op_token = self.current_token()
        operator = ""
        
        if op_token.type == 'ASSIGN':
            operator = '='
            self.eat('ASSIGN')
        
        elif op_token.type in ['PLUS_EQUAL', 'MINUS_EQUAL', 'MULTIPLY_EQUAL', 'DIVIDE_EQUAL']:
            operator = op_token.type
            self.eat(op_token.type)
        
        else:
            raise Exception("Invalid assignment operator")
        
        value = self.parse_expression()
        self.eat('SEMICOLON')
        return Assignment(identifier.value, operator, value)


    def parse_print(self):
        self.eat('PRINT')
        expressions = [self.parse_expression()]
        
        while self.current_token().type == 'COMMA':
            self.eat('COMMA')
            expressions.append(self.parse_expression())
        
        self.eat('SEMICOLON')
        return Print(expressions)


    def parse_if(self):
        conditions = []
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.parse_expression()
        self.eat('RPAREN')
        block = self.parse_block()
        conditions.append((condition, block))
        
        while self.current_token().type == 'ELSE_IF':
            self.eat('ELSE_IF')
            self.eat('LPAREN')
            elif_cond = self.parse_expression()
            self.eat('RPAREN')
            elif_block = self.parse_block()
            conditions.append((elif_cond, elif_block))
        else_block = None
        
        if self.current_token().type == 'ELSE':
            self.eat('ELSE')
            else_block = self.parse_block()
        return If(conditions, else_block)


    def parse_while(self):
        self.eat('WHILE')
        self.eat('LPAREN')
        condition = self.parse_expression()
        self.eat('RPAREN')
        block = self.parse_block()
        return While(condition, block)


    def parse_expression(self):
        return self.parse_equality()


    def parse_equality(self):
        node = self.parse_comparison()
        while self.current_token().type in ['EQUALS', 'NOT_EQUALS']:
            op = self.current_token().type
            self.eat(op)
            right = self.parse_comparison()
            node = BinaryOp(node, op, right)
        return node


    def parse_comparison(self):
        node = self.parse_term()
        
        while self.current_token().type in ['LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL']:
            op = self.current_token().type
            self.eat(op)
            right = self.parse_term()
            node = BinaryOp(node, op, right)
        return node


    def parse_term(self):
        node = self.parse_factor()
        while self.current_token().type in ['PLUS', 'MINUS']:
            op = self.current_token().type
            self.eat(op)
            right = self.parse_factor()
            node = BinaryOp(node, op, right)
        return node


    def parse_factor(self):
        node = self.parse_unary()
        while self.current_token().type in ['MULTIPLY', 'DIVIDE']:
            op = self.current_token().type
            self.eat(op)
            right = self.parse_unary()
            node = BinaryOp(node, op, right)
        return node


    def parse_unary(self):
        if self.current_token().type == 'MINUS':
            self.eat('MINUS')
            return BinaryOp(Literal(0), 'MINUS', self.parse_unary())
        return self.parse_primary()


    def parse_primary(self):
        token = self.current_token()
        
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Literal(token.value)
        
        elif token.type == 'STRING':
            self.eat('STRING')
            return Literal(token.value)
        
        elif token.type == 'BOOLEAN':
            self.eat('BOOLEAN')
            return Literal(token.value)
        
        elif token.type == 'NULL':
            self.eat('NULL')
            return Literal(None)
        
        elif token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return Identifier(token.value)
        
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            expr = self.parse_expression()
            self.eat('RPAREN')
            return expr
        
        else:
            raise Exception(f"Unexpected token {token.type} at line {token.line}, column {token.column}")

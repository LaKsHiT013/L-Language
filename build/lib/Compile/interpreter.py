from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.environment = {}

    def interpret(self, node):
        method_name = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{node.__class__.__name__} method')

    def visit_Program(self, node):
        for stmt in node.statements:
            result = self.interpret(stmt)
            if result in ('break', 'continue'):
                break

    def visit_Block(self, node):
        for stmt in node.statements:
            result = self.interpret(stmt)
            if result in ('break', 'continue'):
                return result

    def visit_VarDecl(self, node):
        value = self.interpret(node.initializer)
        self.environment[node.name] = value

    def visit_Assignment(self, node):
        if node.name not in self.environment:
            raise Exception(f"Undefined variable {node.name}")
        current_val = self.environment[node.name]
        new_val = self.interpret(node.value)
        if node.operator == '=':
            self.environment[node.name] = new_val
        elif node.operator == 'PLUS_EQUAL':
            self.environment[node.name] = current_val + new_val
        elif node.operator == 'MINUS_EQUAL':
            self.environment[node.name] = current_val - new_val
        elif node.operator == 'MULTIPLY_EQUAL':
            self.environment[node.name] = current_val * new_val
        elif node.operator == 'DIVIDE_EQUAL':
            self.environment[node.name] = current_val / new_val

    def visit_Print(self, node):
        outputs = [self.interpret(expr) for expr in node.expressions]
        print(*outputs)

    def visit_If(self, node):
        for cond, block in node.conditions:
            if self.interpret(cond):
                self.interpret(block)
                return
        if node.else_block:
            self.interpret(node.else_block)

    def visit_While(self, node):
        while self.interpret(node.condition):
            result = self.interpret(node.block)
            if result == 'break':
                break
            if result == 'continue':
                continue

    def visit_Break(self, node):
        return 'break'

    def visit_Continue(self, node):
        return 'continue'

    def visit_BinaryOp(self, node):
        left = self.interpret(node.left)
        right = self.interpret(node.right)
        op = node.operator
        if op == 'PLUS':
            return left + right
        elif op == 'MINUS':
            return left - right
        elif op == 'MULTIPLY':
            return left * right
        elif op == 'DIVIDE':
            return left / right
        elif op == 'EQUALS':
            return left == right
        elif op == 'NOT_EQUALS':
            return left != right
        elif op == 'LESS':
            return left < right
        elif op == 'LESS_EQUAL':
            return left <= right
        elif op == 'GREATER':
            return left > right
        elif op == 'GREATER_EQUAL':
            return left >= right
        else:
            raise Exception(f"Unknown binary operator {op}")

    def visit_Literal(self, node):
        return node.value

    def visit_Identifier(self, node):
        if node.name not in self.environment:
            raise Exception(f"Undefined variable {node.name}")
        return self.environment[node.name]

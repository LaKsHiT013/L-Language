class ASTNode:
    def accept(self, visitor):
        method_name = 'visit_' + self.__class__.__name__
        visitor_func = getattr(visitor, method_name, self.generic_visit)
        return visitor_func(self)

    def generic_visit(self, visitor):
        raise Exception(f'No visit_{self.__class__.__name__} method')

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarDecl(ASTNode):
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

class Assignment(ASTNode):
    def __init__(self, name, operator, value):
        self.name = name
        self.operator = operator
        self.value = value

class Print(ASTNode):
    def __init__(self, expressions):
        self.expressions = expressions

class If(ASTNode):
    def __init__(self, conditions, else_block):
        self.conditions = conditions
        self.else_block = else_block

class While(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class Break(ASTNode):
    pass

class Continue(ASTNode):
    pass

class BinaryOp(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Literal(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

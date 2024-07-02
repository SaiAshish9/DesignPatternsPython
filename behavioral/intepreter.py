from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class Number(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number

class Add(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        return self.left_expression.interpret(context) + self.right_expression.interpret(context)

class Subtract(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        return self.left_expression.interpret(context) - self.right_expression.interpret(context)

if __name__ == "__main__":
    context = {}
    expression = Subtract(Add(Number(5), Number(3)), Number(2))
    result = expression.interpret(context)
    print(f"Result: {result}")  # Output: Result: 6

from abc import ABC, abstractmethod

class ComputerPartVisitor(ABC):
    @abstractmethod
    def visit(self, computer_part):
        pass

class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit(self, computer_part):
        if isinstance(computer_part, Computer):
            print("Displaying Computer.")
        elif isinstance(computer_part, Mouse):
            print("Displaying Mouse.")
        elif isinstance(computer_part, Keyboard):
            print("Displaying Keyboard.")
        elif isinstance(computer_part, Monitor):
            print("Displaying Monitor.")

class ComputerPart(ABC):
    @abstractmethod
    def accept(self, computer_part_visitor):
        pass

class Keyboard(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Monitor(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Mouse(ComputerPart):
    def accept(self, computer_part_visitor):
        computer_part_visitor.visit(self)

class Computer(ComputerPart):
    def __init__(self):
        self.parts = [Mouse(), Keyboard(), Monitor()]
    def accept(self, computer_part_visitor):
        for part in self.parts:
            part.accept(computer_part_visitor)
        computer_part_visitor.visit(self)

if __name__ == "__main__":
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())

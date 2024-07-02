from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class WriteCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.write(self.text)

    def undo(self):
        self.receiver.undo_write(self.text)

class TextEditor:
    def __init__(self):
        self.content = ""
        self.history = []

    def write(self, text):
        self.history.append(self.content)
        self.content += text
        print(f"Current content: '{self.content}'")

    def undo_write(self, text):
        if self.history:
            self.content = self.history.pop()
        print(f"Undo: current content: '{self.content}'")

class TextEditorInvoker:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        self.history.append(command)
        command.execute()
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
           
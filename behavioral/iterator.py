from abc import ABC, abstractmethod

# Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Container(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

class NameRepository(Container):
    def __init__(self):
        self.names = ["Robert", "John", "Julie", "Lora"]

    def get_iterator(self):
        return self.NameIterator(self)

    class NameIterator(Iterator):
        def __init__(self, name_repository):
            self._name_repository = name_repository
            self._index = 0

        def has_next(self):
            if self._index < len(self._name_repository.names):
                return True
            return False

        def next(self):
            if self.has_next():
                name = self._name_repository.names[self._index]
                self._index += 1
                return name
            return None

if __name__ == "__main__":
    names_repository = NameRepository()

    iterator = names_repository.get_iterator()
    while iterator.has_next():
        name = iterator.next()
        print(f"Name: {name}")

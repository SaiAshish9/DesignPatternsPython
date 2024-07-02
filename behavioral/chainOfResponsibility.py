from abc import ABC, abstractmethod

class PurchaseHandler(ABC):
    @abstractmethod
    def handle_request(self, amount):
        pass

    def set_successor(self, successor):
        self.successor = successor

class Manager(PurchaseHandler):
    def handle_request(self, amount):
        if amount <= 1000:
            print(f"Manager handles the request for ${amount}")
        elif self.successor:
            self.successor.handle_request(amount)

class Director(PurchaseHandler):
    def handle_request(self, amount):
        if amount <= 5000:
            print(f"Director handles the request for ${amount}")
        elif self.successor:
            self.successor.handle_request(amount)

class VicePresident(PurchaseHandler):
    def handle_request(self, amount):
        if amount <= 10000:
            print(f"Vice President handles the request for ${amount}")
        elif self.successor:
            self.successor.handle_request(amount)

class President(PurchaseHandler):
    def handle_request(self, amount):
        print(f"President handles the request for ${amount}")

if __name__ == "__main__":
    manager = Manager()
    director = Director()
    vice_president = VicePresident()
    president = President()
    manager.set_successor(director)
    director.set_successor(vice_president)
    vice_president.set_successor(president)
    amounts = [500, 1500, 7000, 12000]

    for amount in amounts:
        print(f"\nProcessing purchase request for ${amount}:")
        manager.handle_request(amount)

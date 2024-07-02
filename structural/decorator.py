from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass


class SimpleCoffee(Coffee):
    def cost(self):
        return 5  

class Milk(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2  

class Sugar(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  

if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    print(f"Cost of Simple Coffee: ${simple_coffee.cost()}")

    coffee_with_milk = Milk(simple_coffee)
    print(f"Cost of Coffee with Milk: ${coffee_with_milk.cost()}")

    coffee_with_sugar = Sugar(simple_coffee)
    print(f"Cost of Coffee with Sugar: ${coffee_with_sugar.cost()}")

    coffee_with_milk_and_sugar = Milk(Sugar(simple_coffee))
    print(f"Cost of Coffee with Milk and Sugar: ${coffee_with_milk_and_sugar.cost()}")

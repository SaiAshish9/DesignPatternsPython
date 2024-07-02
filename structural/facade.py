from abc import ABC, abstractmethod

class CoffeeOrder(ABC):
    @abstractmethod
    def serve_coffee(self, context):
        pass

class CoffeeFlavor(CoffeeOrder):
    def __init__(self, flavor):
        self.flavor = flavor

    def serve_coffee(self, context):
        return f"Serving {self.flavor} to table {context.table_number}"

class CoffeeOrderContext:
    def __init__(self, table_number):
        self.table_number = table_number

class CoffeeFlavorFactory:
    flavors = {}

    def get_flavor(self, flavor_name):
        if flavor_name not in self.flavors:
            self.flavors[flavor_name] = CoffeeFlavor(flavor_name)
        return self.flavors[flavor_name]

if __name__ == "__main__":
    orders = [
        ("Espresso", 1),
        ("Cappuccino", 2),
        ("Espresso", 3),
        ("Cappuccino", 4),
        ("Espresso", 5),
    ]

    flavor_factory = CoffeeFlavorFactory()
    for flavor_name, table_number in orders:
        flavor = flavor_factory.get_flavor(flavor_name)
        context = CoffeeOrderContext(table_number)
        print(flavor.serve_coffee(context))

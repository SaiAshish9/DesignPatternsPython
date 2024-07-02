from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

class Stock:
    def __init__(self, name="ABC", quantity=10):
        self.name = name
        self.quantity = quantity

    def buy(self):
        print(f"Stock [ Name: {self.name}, Quantity: {self.quantity} ] bought")

    def sell(self):
        print(f"Stock [ Name: {self.name}, Quantity: {self.quantity} ] sold")

class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class Broker:
    def __init__(self):
        self.order_list = []

    def take_order(self, order):
        self.order_list.append(order)

    def place_orders(self):
        for order in self.order_list:
            order.execute()
        self.order_list.clear()

if __name__ == "__main__":
    abc_stock = Stock()

    buy_stock_order = BuyStock(abc_stock)
    sell_stock_order = SellStock(abc_stock)

    broker = Broker()
    broker.take_order(buy_stock_order)
    broker.take_order(sell_stock_order)

    broker.place_orders()

# Abstract Class
class AbstractCustomer:
    def __init__(self):
        self.name = None

    def is_nil(self):
        pass

    def get_name(self):
        pass

class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_name(self):
        return self.name

    def is_nil(self):
        return False

class NullCustomer(AbstractCustomer):
    def get_name(self):
        return "Not Available in Customer Database"

    def is_nil(self):
        return True

class CustomerFactory:
    names = ["Rob", "Joe", "Julie"]

    @staticmethod
    def get_customer(name):
        for customer_name in CustomerFactory.names:
            if customer_name.lower() == name.lower():
                return RealCustomer(name)
        return NullCustomer()

if __name__ == "__main__":
    customer1 = CustomerFactory.get_customer("Rob")
    customer2 = CustomerFactory.get_customer("Bob")
    customer3 = CustomerFactory.get_customer("Julie")
    customer4 = CustomerFactory.get_customer("Laura")

    print("Customers:")
    print(customer1.get_name())
    print(customer2.get_name())
    print(customer3.get_name())
    print(customer4.get_name())

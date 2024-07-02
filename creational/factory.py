from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

class Bike(Vehicle):
    def create(self):
        return "Bike created"

class Car(Vehicle):
    def create(self):
        return "Car created"

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "bike":
            return Bike()
        elif vehicle_type == "car":
            return Car()
        else:
            return None

# Usage
factory = VehicleFactory()

bike = factory.get_vehicle("bike")
car = factory.get_vehicle("car")

print(bike.create())  # Output: Bike created
print(car.create())   # Output: Car created

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

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass
    
    @staticmethod
    def get_factory(factory_type):
        if factory_type == "bike":
            return BikeFactory()
        elif factory_type == "car":
            return CarFactory()
        else:
            return None

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

# Usage
bike_factory = VehicleFactory.get_factory("bike")
car_factory = VehicleFactory.get_factory("car")

bike = bike_factory.create_vehicle()
car = car_factory.create_vehicle()

print(bike.create())  # Output: Bike created
print(car.create())   # Output: Car created

from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return Car(self.model, self.color)

    def __str__(self):
        return f"Car: Model {self.model}, Color {self.color}"

car_prototype = Car("Prototype Model", "Red")
print(f"Original Car: {car_prototype}")

new_car = car_prototype.clone()
print(f"Cloned Car: {new_car}")

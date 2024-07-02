from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def register(self, obj):
        pass

    @abstractmethod
    def unregister(self, obj):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class DeliveryData(Subject):
    def __init__(self):
        self._observers = []

    def register(self, obj):
        if obj not in self._observers:
            self._observers.append(obj)

    def unregister(self, obj):
        if obj in self._observers:
            self._observers.remove(obj)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._location)

    def location_changed(self):
        self._location = self.get_location()
        self.notify_observers()

    def get_location(self):
        return "YPlace"

class Observer(ABC):
    @abstractmethod
    def update(self, location):
        pass

class Seller(Observer):
    def update(self, location):
        self._location = location
        self.show_location()

    def show_location(self):
        print(f"Notification at Seller - Current Location: {self._location}")

class User(Observer):
    def update(self, location):
        self._location = location
        self.show_location()

    def show_location(self):
        print(f"Notification at User - Current Location: {self._location}")

class DeliveryWarehouseCenter(Observer):
    def update(self, location):
        self._location = location
        self.show_location()

    def show_location(self):
        print(f"Notification at Warehouse - Current Location: {self._location}")

if __name__ == "__main__":
    topic = DeliveryData()
    obj1 = Seller()
    obj2 = User()
    obj3 = DeliveryWarehouseCenter()
    topic.register(obj1)
    topic.register(obj2)
    topic.register(obj3)
    topic.location_changed()
    topic.unregister(obj3)
    print()
    topic.location_changed()

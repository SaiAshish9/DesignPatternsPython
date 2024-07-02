from abc import ABC, abstractmethod

class EmployeeComponent(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Employee(EmployeeComponent):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"{self.position}: {self.name}")

class Manager(EmployeeComponent):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def display_info(self):
        print(f"{self.position}: {self.name}")
        for employee in self.employees:
            employee.display_info()

if __name__ == "__main__":
    developer1 = Employee("John Doe", "Developer")
    developer2 = Employee("Jane Smith", "Developer")
    designer1 = Employee("Emily Brown", "Designer")
    manager1 = Manager("Mike Johnson", "Development Manager")
    manager2 = Manager("Sarah Clark", "Design Manager")
    manager1.add_employee(developer1)
    manager1.add_employee(developer2)
    manager2.add_employee(designer1)
    manager1.display_info()
    manager2.display_info()

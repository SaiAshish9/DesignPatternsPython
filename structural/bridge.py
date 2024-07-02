from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def apply_color(self):
        pass

class RedColor(Color):
    def apply_color(self):
        return "Applying red color"

class GreenColor(Color):
    def apply_color(self):
        return "Applying green color"

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Drawing Circle. {self.color.apply_color()}"

class Square(Shape):
    def draw(self):
        return f"Drawing Square. {self.color.apply_color()}"

if __name__ == "__main__":
    red = RedColor()
    green = GreenColor()

    circle_red = Circle(red)
    square_green = Square(green)

    print(circle_red.draw())
    print(square_green.draw())

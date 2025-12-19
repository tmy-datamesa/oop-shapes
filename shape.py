class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say_name(self):
        print(f"Benim adım {self.name} ve rengim {self.color}.")


class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color) # Üst sınıfa gönderdik
        self.width = width
        self.height = height

    def say_name(self):
        print(f"My name is {self.name} and I am a Rectangle")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    


import math

class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def say_name(self):
        print(f"My name is {self.name} and I am a Circle")

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
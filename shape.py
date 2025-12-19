"""Module providing shape classes for area and perimeter calculations."""
import math

class Shape:
    """Base class for all shapes."""
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        """Returns the name of the shape."""
        return f"My name is {self.name}."

class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, color, name, width, height):
        # Üst sınıfa (Shape) renk ve ismi doğru sırayla gönderiyoruz
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """Returns the specific name and type for rectangle."""
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        """Calculates area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of rectangle."""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, color, name, radius):
        # Üst sınıfa (Shape) renk ve ismi doğru sırayla gönderiyoruz
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """Returns the specific name and type for circle."""
        return f"My name is {self.name} and I am a circle."

    def area(self):
        """Calculates area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates perimeter of circle."""
        return 2 * math.pi * self.radius
    
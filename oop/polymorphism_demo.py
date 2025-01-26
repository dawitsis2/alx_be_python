# polymorphism_demo.py
import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Method to calculate the area of a shape. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override the area method")

class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle (length × width)."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle (π × radius²)."""
        return math.pi * (self.radius ** 2)

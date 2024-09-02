# Code Example:
# Let's say you have a ShapeCalculator class that calculates the area and perimeter of different shapes like rectangles and circles.

class ShapeCalculator:
    
    def calculate_area(self, shape):
        if shape.type == 'rectangle':
            return shape.width * shape.height
        elif shape.type == 'circle':
            return 3.4 * (shape.radius ** 2)
    
    def calculate_perimeter(self, shape):
        if shape.type == 'rectangle':
            return 2 * (shape.width + shape.height)
        elif shape.type == 'circle':
            return 2 * 3.14 * shape.radius
        
    
# If we want to add support for a new shape, like a triangle, we would have to modify the calculate_area and 
# calculate_perimeter methods, violating the Open/Closed Principle.


# To adhere to the OCP, we can create an abstract base class for shapes and separate concrete classes for each shape type:

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    
    def calculate_area(self):
        return self.width * self.height 
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
        
        
class Circle(Shape):
    
    def __init__(self, radius) -> None:
        self.radius = radius
        
    
    def calculate_area(self):
        return 3.4 * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
        if not self._is_valid_triangle():
            raise ValueError("The provided sides do not form a valid triangle")

    def _is_valid_triangle(self):
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)

    def calculate_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def calculate_area(self):
        # Heron's formula: sqrt(s * (s - a) * (s - b) * (s - c))
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))


class ShapeCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()
    
    def calculate_perimeter(self, shape):
        return shape.calculate_perimeter()
    
    
# example usage

shapes = [Rectangle(5, 10), Circle(7), Triangle(5, 5, 5)]

calculator = ShapeCalculator()

for shape in shapes:
    print(f"Area: {calculator.calculate_area(shape)}")
    print(f"Perimeter: {calculator.calculate_perimeter(shape)}")

# By introducing an abstraction (Shape class) and 
# separating the concrete implementations (Rectangle and Circle classes), 
# we can add new shapes without modifying the existing code.

# The ShapeCalculator class can now work with any shape that implements the Shape interface, allowing for easy extensibility.

from abc import ABC, abstractmethod
import math


# Abstract Base Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Vector class
class Vector(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Vector addition
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    # Vector equality
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Compare vector magnitudes
    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def area(self):
        return 0

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Circle class
class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    # Add circle radii
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    # Compare circle radii
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area():.2f})"


# Main program
def main():
    print("===== ABSTRACT SHAPE MATH ENGINE =====")

    print("\n--- Vector Operations ---")
    v1 = Vector(3, 4)
    v2 = Vector(2, 1)

    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Addition:", v1 + v2)
    print("Magnitude of Vector 1:", v1.magnitude())
    print("Are vectors equal?", v1 == v2)
    print("Is Vector 1 smaller than Vector 2?", v1 < v2)

    print("\n--- Circle Operations ---")
    c1 = Circle(5)
    c2 = Circle(3)

    print("Circle 1:", c1)
    print("Circle 2:", c2)
    print("Combined circle:", c1 + c2)
    print("Are circles equal?", c1 == c2)
    print("Is Circle 1 smaller than Circle 2?", c1 < c2)
    print("Area of Circle 1:", round(c1.area(), 2))

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()

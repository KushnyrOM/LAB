from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("Area:", area)

class Rectangle(Shape):
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area:", area)

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area:", area)

# Приклад виклику програми
shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    shape = Circle()
elif shape_type == "rectangle":
    shape = Rectangle()
elif shape_type == "triangle":
    shape = Triangle()
else:
    print("Invalid shape type.")
    exit()

shape.calculate_area()
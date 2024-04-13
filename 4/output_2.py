class FigureInterface:
    def area(self, *args):
        pass

class Square(FigureInterface):
    def area(self, side):
        return side ** 2

class Circle(FigureInterface):
    def area(self, radius):
        return 3.14 * radius ** 2

# Приклад використання класів
square = Square()
print("Area of square:", square.area(5))

circle = Circle()
print("Area of circle:", circle.area(3))
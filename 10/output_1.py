class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Cannot divide by zero")


# Використання
calculator = AdvancedCalculator()
print("Addition:", calculator.add(6, 2))
print("Subtraction:", calculator.subtract(6, 2))
print("Multiplication:", calculator.multiply(6, 2))
print("Division:", calculator.divide(6, 2))
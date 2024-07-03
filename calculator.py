
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

#1
if __name__ == "__main__":
    calc = Calculator()
    print("Addition (3 + 5):", calc.add(3, 5))
    print("Subtraction (10 - 4):", calc.subtract(10, 4))
    print("Multiplication (6 * 7):", calc.multiply(6, 7))
    print("Division (8 / 2):", calc.divide(8, 2))
    try:
        calc.divide(5, 0)
    except ValueError as e:
        print("Division by zero error:", e)

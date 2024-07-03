from calculator_exception import CalculatorException

class Calculator:
    def perform_operation(self, operation, num1, num2):
        if operation == "add":
            return self.add(num1, num2)
        elif operation == "subtract":
            return self.subtract(num1, num2)
        elif operation == "multiply":
            return self.multiply(num1, num2)
        elif operation == "divide":
            return self.divide(num1, num2)
        else:
            raise CalculatorException("Invalid operation.")

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise CalculatorException("Cannot divide by zero.")
        return num1 / num2


from calculator import Calculator
from input_output import InputOutput
from calculator_exception import CalculatorException


def main():
    calculator = Calculator()
    io = InputOutput()

    while True:
        io.display_menu()
        operation = io.get_operation()
        if operation == "exit":
            break

        try:
            num1 = io.get_number("Enter the first number: ")
            num2 = io.get_number("Enter the second number: ")
            result = calculator.perform_operation(operation, num1, num2)
            io.display_result(result)
        except CalculatorException as e:
            io.display_error(str(e))


if __name__ == "__main__":
    main()

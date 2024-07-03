class InputOutput:
    def __init__(self):
        pass

    def display_menu(self):
        print("Calculator Menu:")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("Type 'exit' to quit.")

    def get_operation(self):
        return input("Choose an operation: ")

    def get_number(self, prompt):
        return float(input(prompt))

    def display_result(self, result):
        print("Result:", result)

    def display_error(self, error_message):
        print("Error:", error_message)


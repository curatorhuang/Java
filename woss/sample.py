# sample_code.py

# This function calculates the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# This function reads a file and prints its contents
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    print(content)


# Example usage
if __name__ == "__main__":
    # Test factorial function
    print(factorial(5))  # Should print 120

    # Test read_file function
    read_file("example.txt")  # Ensure there is an example.txt file in the same directory

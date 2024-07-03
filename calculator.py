class Calculator:

    # 加法
    def add(self, a, b):
        return a + b

    # 减法
    def subtract(self, a, b):
        return a - b

    # 乘法
    def multiply(self, a, b):
        return a * b

    # 除法
    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b


if __name__ == "__main__":
    calculator = Calculator()

    a = 10.0
    b = 5.0

    print("加法:", calculator.add(a, b))
    print("减法:", calculator.subtract(a, b))
    print("乘法:", calculator.multiply(a, b))
    print("除法:", calculator.divide(a, b))

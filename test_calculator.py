
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 1) == -1

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 1) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    assert calc.divide(-1, 1) == -1
    assert calc.divide(1, 1) == 1
    try:
        calc.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")


public class Calculator {
    public double performOperation(String operation, double num1, double num2) throws CalculatorException {
        switch (operation) {
            case "add":
                return add(num1, num2);
            case "subtract":
                return subtract(num1, num2);
            case "multiply":
                return multiply(num1, num2);
            case "divide":
                return divide(num1, num2);
            default:
                throw new CalculatorException("Invalid operation.");
        }
    }

    private double add(double num1, double num2) {
        return num1 + num2;
    }

    private double subtract(double num1, double num2) {
        return num1 - num2;
    }

    private double multiply(double num1, double num2) {
        return num1 * num2;
    }

    private double divide(double num1, double num2) throws CalculatorException {
        if (num2 == 0) {
            throw new CalculatorException("Cannot divide by zero.");
        }
        return num1 / num2;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        InputOutput io = new InputOutput();

        while (true) {
            io.displayMenu();
            String operation = io.getOperation();
            if (operation.equals("exit")) {
                break;
            }
//
            try {
                double num1 = io.getNumber("Enter the first number: ");
                double num2 = io.getNumber("Enter the second number: ");
                double result = calculator.performOperation(operation, num1, num2);
                io.displayResult(result);
            } catch (CalculatorException e) {
                io.displayError(e.getMessage());
            }
        }
    }
}

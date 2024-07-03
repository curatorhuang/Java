import java.util.Scanner;

public class InputOutput {
    private Scanner scanner = new Scanner(System.in);

    public void displayMenu() {
        System.out.println("Calculator Menu:");
        System.out.println("1. add");
        System.out.println("2. subtract");
        System.out.println("3. multiply");
        System.out.println("4. divide");
        System.out.println("Type 'exit' to quit.");
    }

    public String getOperation() {
        System.out.print("Choose an operation: ");
        return scanner.nextLine();
    }

    public double getNumber(String prompt) {
        System.out.print(prompt);
        return Double.parseDouble(scanner.nextLine());
    }

    public void displayResult(double result) {
        System.out.println("Result: " + result);
    }

    public void displayError(String errorMessage) {
        System.out.println("Error: " + errorMessage);
    }
}

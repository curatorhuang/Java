public class Calculator {

    // 函数
    public double add(double a, double b) {
        return a + b;
    }

    // 减法
    public double subtract(double a, double b) {
        return a - b;
    }

    // 乘法
    public double multiply(double a, double b) {
        return a * b;
    }

    // 除法
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("除数不能为零");
        }
        return a / b;
    }

    public static void main(String[] args) {
        Calculator calculator = new Calculator();

        double a = 10.0;
        double b = 5.0;

        System.out.println("加法: " + calculator.add(a, b));
        System.out.println("减法: " + calculator.subtract(a, b));
        System.out.println("乘法: " + calculator.multiply(a, b));
        System.out.println("除法: " + calculator.divide(a, b));
    }
}

import java.io.File;
import java.io.FileNotFoundException;
public class testInput {
    String filepath = ".\\src\\main\\java\\org\\example\\operators.txt";

    public static void main(String[] args) {
        System.out.println("test call " + fibonacci(5));
        int a = 3;
        a++;
        a--;
        a++;

    }

    private static int fibonacci(int i) {
        if (i <= 0) return 0;
        System.out.println("i = " + i);
        return fibonacci(i - 1) + fibonacci(i - 2);
    }
}

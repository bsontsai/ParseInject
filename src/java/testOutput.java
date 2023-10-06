static int assignment0 = 0;
static int addition0 = 0;
static int assignment1 = 0;
static int increment0 = 0;
static int decrement0 = 0;
static int increment1 = 0;
static int for0_assignment2 = 0;
static int for0_lessThan0 = 0;
static int for0_increment2 = 0;
static int for0_for1_assignment3 = 0;
static int for0_for1_lessThan1 = 0;
static int for0_for1_increment3 = 0;
static int for0_for1_while0_lessThan2 = 0;
static int for0_for1_while0_increment4 = 0;
static int for2_assignment4 = 0;
static int for2_lessThan3 = 0;
static int for2_increment5 = 0;
static int for2_increment6 = 0;
static int if0_lessThanOrEqual0 = 0;
static int if0_addition1 = 0;
static int if0_subtraction0 = 0;
static int if0_addition2 = 0;
static int if0_subtraction1 = 0;
package java;
import java.io.File;
import java.io.FileNotFoundException;
public class testInput {
assignment0++;
    String filepath = ".\\src\\main\\java\\org\\example\\operators.txt";

    public static void main(String[] args) {
addition0++;
        System.out.println("test call " + fibonacci(5));
assignment1++;
        int a = 3;
increment0++;
        a++;
decrement0++;
        a--;
increment1++;
        a++;
for0_assignment2++;
        for (int i = 0; i < 10; i++) {
for0_for1_assignment3++;
            for (int j = 0; j < 10; j++) {
                while (a < 10) {
for0_for1_while0_increment4++;
                    a++;
for0_for1_while0_lessThan2++;
                }
for0_for1_lessThan1++;
for0_for1_increment3++;
            }
for0_lessThan0++;
for0_increment2++;
        }
for2_assignment4++;
        for (int i = 0; i < 10; i++) {
for2_increment6++;
            a++;
for2_lessThan3++;
for2_increment5++;
        }

    }

    private static int fibonacci(int i) {
if0_lessThanOrEqual0++;
        if (i <= 0) return 0;
if0_addition1++;
        System.out.println("i = " + i);
if0_subtraction0++;
if0_addition2++;
if0_subtraction1++;
        return fibonacci(i - 1) + fibonacci(i - 2);
    }
}

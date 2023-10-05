static int assignment0 = 0;
static int addition0 = 0;
static int assignment1 = 0;
static int increment0 = 0;
static int decrement0 = 0;
static int increment1 = 0;
static int for0_assignment2 = 0;
static int for0_lessThan0 = 0;
static int for0_increment2 = 0;
static int for0_increment3 = 0;
static int for0_if0_equalTo0 = 0;
static int for0_if0_increment4 = 0;
static int for1_assignment3 = 0;
static int for1_lessThan1 = 0;
static int for1_increment5 = 0;
static int for1_increment6 = 0;
static int if1_lessThanOrEqual0 = 0;
static int if1_addition1 = 0;
static int if1_subtraction0 = 0;
static int if1_addition2 = 0;
static int if1_subtraction1 = 0;
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
for0_lessThan0++;
for0_increment2++;
        for (int i = 0; i < 10; i++) {
for0_increment3++;
            a++;
for0_if0_equalTo0++;
            if (a == 2) {
for0_if0_increment4++;
                a++;
            }
        }
for1_assignment3++;
for1_lessThan1++;
for1_increment5++;
        for (int i = 0; i < 10; i++) {
for1_increment6++;
            a++;
        }

    }

    private static int fibonacci(int i) {
if1_lessThanOrEqual0++;
        if (i <= 0) return 0;
if1_addition1++;
        System.out.println("i = " + i);
if1_subtraction0++;
if1_addition2++;
if1_subtraction1++;
        return fibonacci(i - 1) + fibonacci(i - 2);
    }
}

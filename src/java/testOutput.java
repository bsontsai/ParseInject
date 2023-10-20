public class testOutput {
public static int assignment0 = 0;
public static int assignment1 = 0;
public static int increment0 = 0;
public static int decrement0 = 0;
public static int increment1 = 0;
public static int for0_assignment2 = 0;
public static int for0_lessThan0 = 0;
public static int for0_increment2 = 0;
public static int for0_for1_assignment3 = 0;
public static int for0_for1_lessThan1 = 0;
public static int for0_for1_increment3 = 0;
public static int for0_for1_while0_lessThan2 = 0;
public static int for0_for1_while0_increment4 = 0;
public static int for2_assignment4 = 0;
public static int for2_lessThan3 = 0;
public static int for2_increment5 = 0;
public static int for2_increment6 = 0;
public void testInput() {
assignment0++;
    String filepath = ".\\src\\main\\java\\org\\example\\operators.txt";

    System.out.println("test call");
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
}
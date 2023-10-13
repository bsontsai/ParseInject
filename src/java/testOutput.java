package java;
public class testOutput {
static int testInput_assignment0 = 0;
static int testInput_System.out.println0 = 0;
static int testInput_assignment1 = 0;
static int testInput_increment0 = 0;
static int testInput_decrement0 = 0;
static int testInput_increment1 = 0;
static int testInput_for0_assignment2 = 0;
static int testInput_for0_lessThan0 = 0;
static int testInput_for0_increment2 = 0;
static int testInput_for0_for1_assignment3 = 0;
static int testInput_for0_for1_lessThan1 = 0;
static int testInput_for0_for1_increment3 = 0;
static int testInput_for0_for1_while0_lessThan2 = 0;
static int testInput_for0_for1_while0_increment4 = 0;
static int testInput_for2_assignment4 = 0;
static int testInput_for2_lessThan3 = 0;
static int testInput_for2_increment5 = 0;
static int testInput_for2_increment6 = 0;
static int testInput_foo0 = 0;
static int testInput_bar_something0 = 0;
public void testInput() {
testInput_assignment0++;
    String filepath = ".\\src\\main\\java\\org\\example\\operators.txt";

testInput_System.out.println0++;
    System.out.println("test call");
testInput_assignment1++;
    int a = 3;
testInput_increment0++;
    a++;
testInput_decrement0++;
    a--;
testInput_increment1++;
    a++;
testInput_for0_assignment2++;
    for (int i = 0; i < 10; i++) {
testInput_for0_for1_assignment3++;
        for (int j = 0; j < 10; j++) {
            while (a < 10) {
testInput_for0_for1_while0_increment4++;
                a++;
testInput_for0_for1_while0_lessThan2++;
            }
testInput_for0_for1_lessThan1++;
testInput_for0_for1_increment3++;
        }
testInput_for0_lessThan0++;
testInput_for0_increment2++;
    }
testInput_for2_assignment4++;
    for (int i = 0; i < 10; i++) {
testInput_for2_increment6++;
        a++;
testInput_for2_lessThan3++;
testInput_for2_increment5++;
    }
    
testInput_foo0++;
    foo();
    bar() {
        //do something
testInput_bar_something0++;
        something();
    }
}
}
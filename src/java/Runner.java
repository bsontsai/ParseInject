import java.util.ArrayList;
public class Runner {
    public static void main(String[] args) throws IllegalArgumentException, IllegalAccessException, NoSuchFieldException, SecurityException {
        testOutput test = new testOutput();
        ArrayList<String> varList = new ArrayList<>();
        varList.add("assignment0");
        varList.add("assignment1");
        varList.add("increment0");
        varList.add("decrement0");
        varList.add("increment1");
        varList.add("for0_assignment2");
        varList.add("for0_lessThan0");
        varList.add("for0_increment2");
        varList.add("for0_for1_assignment3");
        varList.add("for0_for1_lessThan1");
        varList.add("for0_for1_increment3");
        varList.add("for0_for1_while0_lessThan2");
        varList.add("for0_for1_while0_increment4");
        varList.add("for2_assignment4");
        varList.add("for2_lessThan3");
        varList.add("for2_increment5");
        varList.add("for2_increment6");
        test.testInput();
        for (String var : varList) {
            System.out.println(var + " = " + testOutput.class.getField(var).get(testOutput.class));
        }
    }
}
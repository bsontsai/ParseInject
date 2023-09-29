
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;
public class Parser {

    String operatorsFilepath = ".\\.idea\\src\\operators.txt";
    String inputFilepath = ".\\.idea\\src\\testInput.java";
    Map<String, String> map = new HashMap<>();
    Map<String, Integer> countMap = new HashMap<>();

    public Parser() {
        try {
            BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\benson\\Desktop\\research\\ParseInject\\.idea\\src\\operators.txt"));
            //build operator map
            String line = br.readLine();
            while (line != null) {
//                System.out.println(line);
                String[] split = line.split(",");
                map.put(split[0], split[1]);
                countMap.put(split[0], 0);
                line = br.readLine();
            }
            System.out.println("map");
            System.out.println(map);
            br.close();

            //open file to read
            br = new BufferedReader(new FileReader(inputFilepath));
            line = br.readLine();
            while (line != null) {
                System.out.println(line);
                //check if line is blank
                if (line.equals("")) {
                    line = br.readLine();
                    continue;
                }
                //strip the strings
                line = stripStrings(line);
                //go through the string in pairs of characters
                for (int i = 0; i < line.length() - 1; i++) {
                    String first = String.valueOf(line.charAt(i));
                    String second = String.valueOf(line.charAt(i + 1));
                    String pair = first + second;
                    //see if pair exists in map
                    if (map.containsKey(pair)) {
                        System.out.println("found pair: " + pair);
                        countMap.put(pair, countMap.get(pair) + 1);
                        i++;
                    } else {
                        //check individual character
                        if (map.containsKey(first)) {
                            System.out.println("found single: " + first);
                            countMap.put(first, countMap.get(first) + 1);
                        }
                    }
                }
                //check last character
                String lastChar = String.valueOf(line.charAt(line.length() - 1));
                if (map.containsKey(lastChar)) {
                    System.out.println("found single: " + lastChar);
                    countMap.put(lastChar, countMap.get(lastChar) + 1);
                }
                line = br.readLine();
            }
            System.out.println("countMap");
            System.out.println(countMap);
        } catch (Exception e) {
            System.out.println("exception in Parser constructor");
        }

    }

    private static String stripStrings(String line) {
        //removes all stuff enclosed in ""
        StringBuilder moddedLine = new StringBuilder();
        boolean append = true;
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '\\') continue;
            if (line.charAt(i) == '\"') {
                append = !append;
                moddedLine.append('\"');
                continue;
            }
            if (append) moddedLine.append(line.charAt(i));
        }

        return moddedLine.toString();
    }

    public static void main(String[] args) {
        String string = "String str = \"hello this should not be there\";";
        System.out.println(stripStrings(string));
    }
}

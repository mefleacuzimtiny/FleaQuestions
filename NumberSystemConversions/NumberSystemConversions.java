import java.lang.reflect.Array;
import java.util.*;

public class NumberSystemConversions {
    public static Map<Integer,Character> SYMBOLS;
    public static Random randobj = new Random();
    public static Map<Integer,String> NUMSYSNAMES;
    public static Scanner readobj = new Scanner(System.in);

    // static initialization block. Allows to prevent the need for .initSymbols()
    // to put all the values in. So no need to call .initSymbols() in .main() either
    static {
        HashMap<Integer, Character> mutableMap = new HashMap<>();
        mutableMap.put(0, '0');
        mutableMap.put(1, '1');
        mutableMap.put(2, '2');
        mutableMap.put(3, '3');
        mutableMap.put(4, '4');
        mutableMap.put(5, '5');
        mutableMap.put(6, '6');
        mutableMap.put(7, '7');
        mutableMap.put(8, '6');
        mutableMap.put(9, '9');
        mutableMap.put(10, 'A');
        mutableMap.put(11, 'B');
        mutableMap.put(12, 'C');
        mutableMap.put(13, 'D');
        mutableMap.put(14, 'E');
        mutableMap.put(15, 'F');
        SYMBOLS = Map.copyOf(mutableMap);

        HashMap<Integer, String> numsysMutableMap = new HashMap<>();
        numsysMutableMap.put(2, "Bin");
        numsysMutableMap.put(8, "Oct");
        numsysMutableMap.put(10, "Dec");
        numsysMutableMap.put(16, "Hex");
        NUMSYSNAMES = Map.copyOf(numsysMutableMap);
    }

    public static String lineIn(String prompt) {
        System.out.print(prompt);
        return readobj.nextLine();
    }
    public static String lineIn() {
        return readobj.nextLine();
    }

    public static double keepDecimal(double value) {
        return value - (int) value;
    }

    public static String convertSys(double value, int base, int precision) {
        String whole = "";
        String fractional = "";

        int val = (int) value;
        while (val > 0) {
            whole = SYMBOLS.get( val % base ) + whole;
            val = val / base;
        }

        // need to make frac correct to `precision` decimal places
        double frac = keepDecimal(value);
        for (int i = 0; i < precision; i++) {
            frac = base * keepDecimal(frac);
            fractional += SYMBOLS.get((int)frac);
        }

        if (fractional == "") {
            return whole;
        }
        return whole + "." + fractional;
    }

    public static ArrayList<Integer> selectUniqueRandomInts(Set<Integer> int_set, int size) {
        ArrayList<Integer> toShuffle = new ArrayList<>();
        for (int i : int_set) {
            toShuffle.add(i);
        }
        Collections.shuffle(toShuffle);
        ArrayList<Integer> toReturn = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            toReturn.add(toShuffle.get(i));
        }
        return toReturn;
    }

    public static void genQuestion() {
        double value = randobj.nextDouble(0, 500);
        ArrayList<Integer> bases = selectUniqueRandomInts(NUMSYSNAMES.keySet(), 2);

        int prec_answer = randobj.nextInt(0, 8);
        int prec_question = (int) Math.ceil (prec_answer * (Math.log(bases.get(1)) / Math.log(bases.get(0)) ));

        String converted = convertSys(value, bases.get(0), prec_question);
        String answer = convertSys(value, bases.get(1), prec_answer);

        System.out.println("Precision: " + prec_answer + " decimal places");
        System.out.println("Convert " + NUMSYSNAMES.get(bases.get(0)) + " " + converted + " to " + NUMSYSNAMES.get(bases.get(1)) );

        String toCheck = lineIn("Enter your answer: ");

        if (answer.equals(toCheck)) {
            System.out.println("Yes, your answer is correct");
        } else {
            System.out.println("Incorrect answer. The correct answer was " + answer);
        }
    }


    //Todo: Add a timer countdown and a difficulty functionality
    public static void main(String[] args) {
        String q = "";
        while (! q.equals("q")) {
            genQuestion();
            q = lineIn();
        }
    }
}
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'hackerrankInString' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    private static String helper (String s, String compare) {
            if (compare == ""){
                return "YES";
            }
            else if (s == ""){
                return "NO";
            }
            else if (s.charAt(0) == compare.charAt(0)) {
                if (compare.length() == 1){
                    return "YES";
                }
                compare = compare.substring(1,compare.length());
                return helper(s.substring(1,s.length()),compare);
            }
            else {
                
                return helper(s.substring(1,s.length()),compare);
            }
            }

    public static String hackerrankInString(String s) {
    // Write your code here
        
        String compare = "hackerrank";
        
        return helper(s,compare);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s = bufferedReader.readLine();

                String result = Result.hackerrankInString(s);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

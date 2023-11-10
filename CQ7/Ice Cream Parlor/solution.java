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
import  javafx.util.Pair;

class Result {

    /*
     * Complete the 'icecreamParlor' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER m
     *  2. INTEGER_ARRAY arr
     */

    public static Integer icecreamParlor(int m, List<Integer> arr) {
    // Write your code here
        
        
        return helper(m, arr, 0, 0);
        
    }
    
    public static Integer helper(int m, List<Integer> arr, int current,int picked) {
    // Write your code here
        
        if (m == 0 && picked == 2) {
            return 1;   
        }
        else if (current >= arr.size()){
            return 0;
        }
        else if (m - arr.get(current) < 0){
            return helper(m,arr,current+1,picked);
            }
        else {
            return helper(m,arr,current+1,picked) + helper(m - arr.get(current),arr,current+1,picked + 1);
        }
        
        
    }

}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                int m = Integer.parseInt(bufferedReader.readLine().trim());

                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                    .map(Integer::parseInt)
                    .collect(toList());

                Integer result = Result.icecreamParlor(m, arr);
                bufferedWriter.write(result.toString() + "\n");
                
                // bufferedWriter.write(
                //     result.stream()
                //         .map(Object::toString)
                //         .collect(joining(" "))
                //     + "\n"
                // );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}
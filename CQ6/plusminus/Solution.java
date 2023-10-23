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
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
        float pos = 0;
        float neg = 0;
        float zer = 0;
        float size = arr.size();
        float cur = 0;
        for (int i=0; i < size;i++){
            cur = arr.get(i);
            if (cur > 0){
                pos+=1;
                }
            else if (cur < 0){
                neg+=1;
                }
            else {
                zer+=1;
                }
        }
        
        DecimalFormat df = new DecimalFormat("#.######");
        
        System.out.println(df.format(pos/size));
        System.out.println(df.format(neg/size));
        System.out.println(df.format(zer/size));
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}

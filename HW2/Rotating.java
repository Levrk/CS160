public class Rotating {
    public static void rotatingString(String s) {
        int n = s.length();
        // loop through each rotation to be produced
        for (int i = 1; i < n; i++) {
            String rotated = "";
            // loop through the characters to be added to each rotation
            for (int j = i; j < n; j++) {
                rotated += s.charAt(j);
            }
            // add initial characters
            rotated += s.substring(0, i);
            System.out.print(rotated);
            System.out.print(" ");
        }
        // print last rotation (original string)
        System.out.print(s);
        System.out.println();
    }


    public static void main(String[] args) {
        // parse the command line argument with the number of strings to be rotated
        int q = Integer.parseInt(args[0]);
        // parse the command line strings and call rotatingString
        for (int i = 1; i <= q; i++) {
            rotatingString(args[i]);
        }
    }
}

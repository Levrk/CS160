public class Rotating {
    public static void rotatingString(String s) {
        int n = s.length();

        for (int i = 1; i < n; i++) {
            String rotated = "";
            for (int j = i; j < n; j++) {
                rotated += s.charAt(j);
            }
            rotated += s.substring(0, i);
            System.out.print(rotated);
            System.out.print(" ");
        }
        System.out.print(s);
        System.out.println();
    }


    public static void main(String[] args) {
        int q = Integer.parseInt(args[0]);
        for (int i = 1; i <= q; i++) {
            rotatingString(args[i]);
        }


        //BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        //int q = Integer.parseInt(bufferedReader.readLine().trim());
//        Scanner scanner = new Scanner(System.in);
//        int q = scanner.nextInt();
//
//        IntStream.range(0, q).forEach(qItr -> {
//            String s = scanner.nextLine();
//            rotatingString(s);
//        });

        //bufferedReader.close();
    }
}

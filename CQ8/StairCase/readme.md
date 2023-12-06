    public static void staircase(int n) {
        // Write your code here
            for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= n - i; j++) {
                        System.out.print(" ");
                    }
                    for (int k = 1; k <= i; k++) {
                        System.out.print("#");
                    }
                    System.out.println();
                }
        }


Time Complexity

This function is n^2 time complexity because the external loop runs n times and then the internal loops run a total of n times as well. multiplied together this gives us a time complexity of n^2

Space Complexity:
The space complexity of this function is constant because we are not defining any variables or doing anything that would take up space

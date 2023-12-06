public static int helper(String s, int index, int count) {  
        if (index == s.length()) {
            return count;
        }
        if (s.charAt(index) == s.charAt(index - 1)) {
            count++;
        }
        return helper(s, index + 1, count);

        }

    public static int alternatingCharacters(String s) { 
        int output = (helper(s,1,0));
        return output;
    }


Time Complexity:

this function run's in linear time complexity because the recursive helper function is called once for each letter in the input string s and it does not contain any for loops or logic structures which would impact time complexity. For this reason my recursive implementation functions in linear time executing its helper function once per letter in string S


Space Complexity 

This function runs in constant space complexity because it defines its output variable outside of the recursive calls. This means that space does not have to be reallocated for the output variable each time the function is executed but only once at the begining. For this reason the function has constant space complexity.
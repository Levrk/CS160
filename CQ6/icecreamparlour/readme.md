Psuedo Code:

public static List<Integer> helper(int current,int target, List<Integer> arr,List<Integer> chosen, int closest, List<Integer>) {
        List<Integer> empty = new ArrayList<>();
        //if we have succeded
            if (target <= minimum && chosen.size()==3){
                if target < minimum
                    return new ArrayList<>(chosen);
                else: 
            }
        //if we have failed
            if (current >= arr.size() || target < 0){
                return acc.get(-1);
            }
        //if we dont include
        List<Integer> y = helper(current+1,target, arr, chosen);
        //if we include
        chosen.add(current+1);
        int nextTarget = target - arr.get(current)
        if nextTarget
        List<Integer> x = helper(current+1,nextTarget, arr, chosen);
        chosen.remove(chosen.size() - 1);
        //return whichever is not empty
        if (!x.isEmpty()){
             return x;
        }
       else {return y;}
    } 

Ice Cream Parlour (currentIndex, Target, arr, chosen, closest, acc)
    // if we have found a grouping which is closer than the previous closeness
    if (target < minimum && chosen.size() == 3)
        add chosen to acc and recall the function at the next index 
    //if we are finished
    if (current >= arr.size() || target < 0)
        return the last item in acc
    // if we include 
    int nextTarget = target - arr.get(current)
    
    x = helper(current+1,nextTarget, arr, chosen);


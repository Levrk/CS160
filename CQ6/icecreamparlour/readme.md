Psuedo Code:

Ice Cream Parlour (currentIndex, Target, arr, chosen, closest, acc)
    // if we have found a grouping which is closer than the previous closeness
    if (target < minimum && chosen.size() == 3)
        add chosen to acc and recall the function at the next index 
    //if we are finished
    if (current >= arr.size() || target < 0)
        return the last item in acc

    //if we dont include
    y = helper(current+1,target, arr, chosen, closest, acc);

    // if we include 
    int nextTarget = target - arr.get(current)
    chosen.add(current+1);

    if nextTarget < closest                 // we must update the closest in the next call
    x = helper(current+1,nextTarget, arr, chosen, nextTarget, acc);
    else
    x = helper(current+1,nextTarget, arr, chosen, closest, acc);

    return x;


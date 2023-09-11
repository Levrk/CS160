public class sep8 {

public static int iterative(int arr[], int e){


    for (int i = 0 ; i < arr.length;i++){
        if (arr[i] == e) {
            return i;
        }
    }
    return -1;

}

public static int recursive(int arr[], int e, int c){

    if (arr.length == 0) { return -1; }
    else if (arr[0] = 0) { return -1; }
    else { return recursive}
    
    return -1;

}


public static void main (String[] args){

    int arr[] = new int[]{1,2,3,4,5};

    System.out.println(iterative(arr,3));


}

}
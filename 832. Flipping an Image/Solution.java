class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int index = 0;
        while(index < A.length){
            int[] arr = A[index];
            for (int i = 0; i<arr.length/2;i++){
                int temp = arr[i];
                arr[i] = arr[arr.length -i -1];
                arr[arr.length -i -1] = temp;
            }
            int i = 0;
            while(i<arr.length){
                if(arr[i] == 1){arr[i]=0;}
                else{arr[i]=1;}
                i++;
            }
            index++;
        }
        return A;
    }
}

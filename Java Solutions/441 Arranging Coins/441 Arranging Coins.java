class Solution {
    public int arrangeCoins(int n) { 
        int counter = 0;
        for(int i = 1; n>=0;i++){
            n=n-i;
            if(n>=0){
                counter++;
            }            
        }
        return counter;
    }
}

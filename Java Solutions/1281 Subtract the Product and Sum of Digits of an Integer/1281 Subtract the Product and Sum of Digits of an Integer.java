class Solution {
    public int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        String number = Integer.toString(n);
        for (int i =0;i<number.length();i++){
            product = product * Character.getNumericValue(number.charAt(i)); 
            sum += (Character.getNumericValue(number.charAt(i)));
        }
    return product-sum;
    }
}

class Solution {
    public int titleToNumber(String s) {
        int output=0;
        for(char c:s.toCharArray()){
            output = output * 26+(c-65)+1;
        }
        return output;
    }
}

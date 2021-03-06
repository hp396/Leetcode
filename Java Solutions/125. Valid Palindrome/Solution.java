class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("\\p{Punct}","").toLowerCase().replaceAll(" ","");
        if(s.equals(new StringBuffer(s).reverse().toString())){
            return true;
        }else{return false;}
    }
}
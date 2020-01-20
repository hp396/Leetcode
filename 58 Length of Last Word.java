class Solution {
    public int lengthOfLastWord(String s) {
        String[] last = s.split(" ");
        if (last.length<=0){return 0;}
        return last[last.length-1].length();
    }
}

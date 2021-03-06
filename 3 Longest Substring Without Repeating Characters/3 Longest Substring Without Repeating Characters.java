class Solution {
    public int lengthOfLongestSubstring(String s) {
        ArrayList<ArrayList<Character>> alllist= new ArrayList<ArrayList<Character>>();
        while(!s.isEmpty()) {
            ArrayList<Character> answerlist = new ArrayList<Character>();
            for (char eachletter : s.toCharArray()) {
                if (!answerlist.contains(eachletter)) {
                    answerlist.add(eachletter);
                } else {
                    break;
                }
            }
            alllist.add(answerlist);
            s = s.substring(1);
        }
        int q = 0;
        for (ArrayList<Character> lists:alllist){
            if (lists.size()>q){
                q = lists.size();
            }
        }
        return q;
    }
}

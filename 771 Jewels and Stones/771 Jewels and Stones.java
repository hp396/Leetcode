import java.util.ArrayList;
class Solution {
    public int numJewelsInStones(String J, String S) {
        int counter = 0;
        for (char c:S.toCharArray()){
            //System.out.println(c);
            if (J.contains(Character.toString(c))){
                counter++;
            }
        }
        return counter;
    }
}

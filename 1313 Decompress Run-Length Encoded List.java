import java.util.ArrayList;

class Solution {
    public int[] decompressRLElist(int[] nums) {
        ArrayList<Integer> intList = new ArrayList<Integer>(nums.length);
        for (int i : nums) {intList.add(i);}
        
        ArrayList<Integer> output = new ArrayList<Integer>();
        while(!intList.isEmpty()){
            int freq = intList.get(0);
            int val = intList.get(1);
            intList.remove(1);
            intList.remove(0);
            int i = 0;
            while(i<freq){
                output.add(val);
                i++;
            }
        }
        int[] arr = output.stream().mapToInt(i -> i).toArray();
    return arr;
    }
}

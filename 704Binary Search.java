import java.util.Arrays;
class Solution {
    public int search(int[] nums, int target) {
        int index = -1;
        if(IntStream.of(nums).anyMatch(x -> x == target)){
            for(int i =0;i<nums.length;i++){
                if(nums[i]==target){
                    index = i;
                }
            }
        }  
        return index;
    }

}

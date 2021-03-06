class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> output = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 1;i<nums.length;i++){
            if (nums[i]==nums[i-1]){
                output.add(nums[i]);
            }
        }
        return output;
    }
}
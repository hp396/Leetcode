class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        output = 0
        while i < len(nums):
            output += min(nums[i:i+2])
            i+=2
        return output

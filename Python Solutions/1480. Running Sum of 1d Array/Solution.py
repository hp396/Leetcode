class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = 0
        i = 0
        while i < len(nums):
            output += nums[i]
            nums[i] = output
            i +=1
        return nums
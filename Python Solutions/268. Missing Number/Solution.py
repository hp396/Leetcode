class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums =set(nums)
        x = int(len(nums))
        for i in range(0,x+1):
            if i not in nums:
                return i
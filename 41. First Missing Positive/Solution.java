class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = int(len(nums))+2
        nums = set(nums)
        for i in range(1,x):
            if i not in nums:
                return i

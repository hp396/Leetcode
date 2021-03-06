class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #48ms 90.15, 13.7mb 76.92
        nums = list(dict.fromkeys(nums))
        if len(nums)<3:
            return max(nums)
        nums.sort()
        return nums[-3]
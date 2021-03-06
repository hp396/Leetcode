class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxele = max(nums)
        index = nums.index(maxele)
        nums.remove(maxele)
        for i in nums:
            if ((maxele >= 2*i) is not True):
                return -1
        return index

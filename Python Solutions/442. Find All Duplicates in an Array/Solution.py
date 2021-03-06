class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # duplicate = list()
        output = list()
        nums.sort()
        i = 1
        while i <int(len(nums)):
            if nums[i] == nums[i-1]:
                output.append(nums[i])
            i+=1
        return output
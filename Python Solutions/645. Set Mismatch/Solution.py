class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:      
        output = []
        for i in range(0,len(nums)):
            if nums[i] in nums[i+1:]:
                output.append(nums[i])
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                output.append(i)
                break
        return output
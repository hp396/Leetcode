class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = int(len(nums))+1
        if nums == []:
            return nums
        nums = set(nums)
        output = []
        for i in range(1,x):
            if ((i not in nums)):
                output.append(i)
        return output
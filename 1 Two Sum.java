class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:     
        index= 0
        removedcounter=0
        while True:
            num = nums[0]
            nums.pop(0)
            removedcounter+=1
            for i in nums:
                # num2i+=1
                if num + i == target:
                    num2i = nums.index(i) + removedcounter
                    return [index,num2i]
            index+=1

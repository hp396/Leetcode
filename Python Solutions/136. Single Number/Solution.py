class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = set()
        
        for i in nums:
            if i in num:
                num.remove(i)
            else:
                num.add(i)
        if len(num) ==0:
            return 0
        for i in num:
            return i
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        for num in  nums:
            strnum = str(num)
            if int(len(strnum))%2==0:
                output+=1
        return output
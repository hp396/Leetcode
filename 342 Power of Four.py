class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        res = math.log(num)/math.log(4)
        if res.is_integer():
            return True
        else: return False

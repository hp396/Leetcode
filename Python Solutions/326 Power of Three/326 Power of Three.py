class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        res =math.log10(n)/math.log10(3)
        if res.is_integer():
            return True
        else: return False

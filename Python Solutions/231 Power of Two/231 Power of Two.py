class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        res = (math.log10(n)/math.log10(2))
        if res.is_integer():
            return True
        else: return False

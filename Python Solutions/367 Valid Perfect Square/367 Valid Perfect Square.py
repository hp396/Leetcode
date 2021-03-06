class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**(1/2)).is_integer():
            return True
        else: return False

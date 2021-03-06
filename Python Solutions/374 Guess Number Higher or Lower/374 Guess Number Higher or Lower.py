# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return int(self.binsearch(n,n/2,1))
            
    def binsearch(self,n,mid,start):
        output = guess(mid)
        if output == 0:
            return mid
        elif output == -1:
            return self.binsearch(mid,mid/2,start)
        elif output == 1:
            return self.binsearch(n,(n+mid)/2,mid)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 0
        end = n
        while start<end:
            mid = start + (end-start)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start
        """
        :type n: int
        :rtype: int
        """
        
        
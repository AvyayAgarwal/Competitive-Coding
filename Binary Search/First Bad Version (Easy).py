# 278. First Bad Version - Easy
# Tags - Binary Search

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while(left <= right):
            mid = (right+left)//2
            midres = isBadVersion(mid)
            
            if(midres is True):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
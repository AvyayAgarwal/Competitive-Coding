# 367. Valid Perfect Square - Easy
# Tags - Math, Binary Search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = num ** (0.5)
        return ((num!=0) and ((res%1)==0))
# 231. Power of Two - Easy
# Tags - Math, Bit Manipulation

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 2**int(log(n,2)) == n if n > 0 else False
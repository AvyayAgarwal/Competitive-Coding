# 338. Counting Bits - Medium
# Tags - Dynamic Programming (DP), Bit Manipulation

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i//2] + (i % 2)
        return res
# 945. Minimum Increment to Make Array Unique - Medium
# Tags - Array

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        curr = -1
        res = 0
        A.sort()
        for num in A:
            if curr < num:
                curr = num
            else:
                curr += 1
                res = res + curr - num
        return res
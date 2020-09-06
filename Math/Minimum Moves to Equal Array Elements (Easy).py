# 453. Minimum Moves to Equal Array Elements - Easy
# Tags - Math

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        res = 0
        for i in range(len(nums)):
            res += nums[i] - mn
        return res
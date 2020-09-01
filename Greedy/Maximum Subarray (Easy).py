# 53. Maximum Subarray - Easy
# Tags - Greedy (not listed), Divide and Conquer, Dynamic Programming (DP), Array

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        curr = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            res = max(res, curr)
        return res
# 713. Subarray Product Less Than K - Medium
# Tags - Array, Two Pointers

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        left = 0
        product = 1
        for right, val in enumerate(nums):
            product = product * val
            while product >= k:
                product = product // nums[left]
                left += 1
            res = res + right - left + 1
        return res
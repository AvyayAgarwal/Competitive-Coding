# 560. Subarray Sum Equals K - Medium
# Tags - Array, Hash Table

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = collections.defaultdict(int)
        count = 0
        sum = 0
        map[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            count += map[sum - k]
            map[sum] = map[sum] + 1
        return count
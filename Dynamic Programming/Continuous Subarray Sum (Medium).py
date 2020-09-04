# 523. Continuous Subarray Sum - Medium
# Tags - Math, Dynamic Programming

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        map = dict()
        map[0] = -1
        
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum = sum % k
            if sum in map and (i - map[sum] > 1):
                return True
            if sum not in map:
                map[sum] = i
            
        return False
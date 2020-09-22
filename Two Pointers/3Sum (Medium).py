# 15. 3Sum - Medium
# Tags - Array, Two Pointers, Hash Table

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo = i + 1
            hi = len(nums) - 1
            
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum > 0:
                    hi -= 1
                elif sum < 0:
                    lo += 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi-1] == nums[hi]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return res
                    
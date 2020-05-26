# 525. Contiguous Array - Medium
# Tags - Hash Table

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        countmap = {0: -1}
        count = 0
        res = 0
        
        for i in range(len(nums)):
            count += 1 if nums[i]==1 else -1
            if count in countmap:
                res = max(res, i - countmap[count])
            else:
                countmap[count] = i
        
        return res
# 1365. How Many Numbers Are Smaller Than the Current Number - Easy
# Tags - Array, Hash Table

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortarr = sorted(nums)
        res = []
        for num in nums:
            res.append(sortarr.index(num))
        return res
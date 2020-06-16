# 26. Remove Duplicates from Sorted Array - Easy
# Tags - Array, Two Pointers

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0 : return 0
        endptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[endptr]:
                endptr += 1
                nums[endptr] = nums[i]
        return endptr + 1
# 540. Single Element in a Sorted Array - Medium
# Tags - Binary Search (none mentioned on LeetCode)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            mid = (left+right)//2
            if((mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1])):
               left = mid + 1
            else:
               right = mid
        return nums[left]
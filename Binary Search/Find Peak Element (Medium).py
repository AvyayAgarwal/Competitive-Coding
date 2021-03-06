# 162. Find Peak Element - Medium
# Tags - Array, Binary Search

class Solution:
    def recurse(self, nums: List[int], low: int, high: int):
        mid = (low + high) // 2
        if(low == high):
            return low
        elif(nums[mid] >= nums[mid+1]):
            return self.recurse(nums, low, mid)
        else:
            return self.recurse(nums, mid + 1, high)
       
        
    def findPeakElement(self, nums: List[int]) -> int:
        return self.recurse(nums, 0, len(nums)-1)

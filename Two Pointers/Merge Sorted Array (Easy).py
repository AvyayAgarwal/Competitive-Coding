# 88. Merge Sorted Array - Easy
# Tags - Array, Two Pointers

# Note - Can be improved and cleaned

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while True:
            print(nums1)
            if i == m:
                nums1[m+j:] = nums2[j:]
                break
            if(j == n):
                break
                
            if(nums2[j] <= nums1[i+j]):
                nums1.insert(i+j, nums2[j])
                nums1.pop()
                j += 1
            else:
                i += 1
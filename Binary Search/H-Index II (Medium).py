# 275. H-Index II - Medium
# Tags - Binary Search

class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        n = len(citations)
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] + mid >= n:
                right = mid - 1
            else:
                left = mid + 1                
        return n - left
        
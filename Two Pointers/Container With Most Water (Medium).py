# 11. Container With Most Water - Medium
# Tags - Array, Two Pointers

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            area = max(area, (end - start)*min(height[start], height[end]))
            if(height[start] < height[end]):
                start += 1
            else:
                end -= 1
        return area
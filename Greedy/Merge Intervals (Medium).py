# 56. Merge Intervals - Medium
# Tags - Greedy, Array, Sort

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        
        for i in range(1, n):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1
        
        return res
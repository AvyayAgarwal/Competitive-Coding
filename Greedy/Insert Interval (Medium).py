# 57. Insert Interval - Medium
# Tags - Greedy, Array, Sort

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        if n == 0:
            return [newInterval]
        
        while i < n and newInterval[0] > intervals[i][0]:
            res.append(intervals[i])
            i += 1
        
        if len(res) > 0 and res[-1][1] >= newInterval[0]:
                res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval)
            
        while i < n:
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
            i += 1
        
        return res
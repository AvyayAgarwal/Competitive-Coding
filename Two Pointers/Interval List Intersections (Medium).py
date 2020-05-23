# 986. Interval List Intersections - Medium
# Tags - Two Pointers

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        Alen = len(A)
        Blen = len(B)
        i = 0
        j = 0
        res = []
        while(i < len(A) and j < len(B)):            
            lower = max(A[i][0], B[j][0])
            higher = min(A[i][1], B[j][1])
            if(lower <= higher):
                res.append([lower, higher])
            if(A[i][1] <= B[j][1]):
                i += 1
            else:
                j += 1
        return res
# 918. Maximum Sum Circular Subarray - Medium
# Tags - Array

class Solution:
    def calcKadane(self, A: List[int]) -> int:
        currMax = A[0]
        totalMax = A[0]
        for i in range(1, len(A)):             
            if (currMax < 0): 
                currMax = 0
            currMax = currMax + A[i]
            if (totalMax < currMax): 
                totalMax = currMax 
        return totalMax 
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        kadsum = self.calcKadane(A)
        
        circsum = 0
        for i,v in enumerate(A):
            circsum += v
            A[i] = -v
        circsum += self.calcKadane(A)
        
        if(circsum > kadsum and circsum != 0):
            return circsum
        else:
            return kadsum
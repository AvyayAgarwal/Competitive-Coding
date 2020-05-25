# 1035. Uncrossed Lines - Medium
# Tags - Array

# Note - Can be made efficient with Dynamic Programming (DP)

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:    
        Alen = len(A)
        Blen = len(B)
        dp = [[0 for y in range(Blen+1)] for x in range(Alen+1)]
        
        for i in range(Alen - 1, -1, -1):
            for j in range(Blen - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return dp[0][0]
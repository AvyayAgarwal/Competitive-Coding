# 62. Unique Paths - Medium
# Tags -  Array, Dynamic Programming (DP)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                else:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
                
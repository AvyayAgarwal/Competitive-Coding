# 72. Edit Distance - Hard
# Tags - String, Dynamic Programming (DP)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
        
        for i in range(len1, -1, -1):
            for j in range(len2, -1, -1):
                if i == len1:
                    dp[i][j] = len2 - j
                elif j == len2:
                    dp[i][j] = len1 - i
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) + 1
        
        return dp[0][0]
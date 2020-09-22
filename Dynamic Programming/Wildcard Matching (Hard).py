# 44. Wildcard Matching - Hard
# Tags - String, Dynamic Programming (DP), Backtracking, Greedy

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        newp = ""
        for ch in p:
            if len(newp) == 0:
                newp += ch
            elif ch == "*" and newp[-1] == "*":
                continue
            else:
                newp += ch
        
        dp = [[False for _ in range(len(newp) + 1)] for _ in range(len(s) + 1)]
        
        dp[0][0] = True
        if len(newp) > 0 and newp[0] == '*':
            dp[0][1] = True
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == newp[j-1] or newp[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif newp[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
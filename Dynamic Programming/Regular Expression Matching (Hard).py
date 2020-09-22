# 10. Regular Expression Matching - Hard
# Tags - String, Dynamic Programming (DP), Backtracking

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        # def recurse(sid, pid):
        #     if dp[sid][pid] == None:
        #         if pid == len(p):
        #             dp[sid][pid] = sid == len(s)
        #         else:
        #             curr = False if sid == len(s) else (p[pid] == '.' or p[pid] == s[sid])
        #             if pid + 1 < len(p) and p[pid+1] == "*":
        #                 dp[sid][pid] = recurse(sid, pid+2) or (curr and recurse(sid+1,pid))
        #             else:
        #                 dp[sid][pid] = curr and recurse(sid+1, pid+1)
        #     return dp[sid][pid]
        # return recurse(0,0)
        
        
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(dp[0])):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
                
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
                
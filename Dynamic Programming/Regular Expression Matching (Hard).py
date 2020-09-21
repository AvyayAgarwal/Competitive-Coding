# 10. Regular Expression Matching - Hard
# Tags - String, Dynamic Programming (DP), Backtracking

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        def recurse(sid, pid):
            if dp[sid][pid] == None:
                if pid == len(p):
                    dp[sid][pid] = sid == len(s)
                else:
                    curr = False if sid == len(s) else (p[pid] == '.' or p[pid] == s[sid])
                    if pid + 1 < len(p) and p[pid+1] == "*":
                        dp[sid][pid] = recurse(sid, pid+2) or (curr and recurse(sid+1,pid))
                    else:
                        dp[sid][pid] = curr and recurse(sid+1, pid+1)
            return dp[sid][pid]
        return recurse(0,0)
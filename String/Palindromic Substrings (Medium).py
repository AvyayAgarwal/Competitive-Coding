# 647. Palindromic Substrings - Medium
# Tags - String, Dynamic Programming (DP)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for mid in range(2*n - 1):
            lo = mid // 2
            hi = lo + mid % 2
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                res += 1
                lo -= 1
                hi += 1
        return res
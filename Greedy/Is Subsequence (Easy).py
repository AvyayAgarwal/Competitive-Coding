# 392. Is Subsequence - Easy
# Tags - Greedy, Dynamic Programming, Binary Search

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prevSearchIndex = -1
        for ch in s:
            i = t.find(ch, prevSearchIndex + 1)
            if i == -1:
                return False
            prevSearchIndex = i
        return True
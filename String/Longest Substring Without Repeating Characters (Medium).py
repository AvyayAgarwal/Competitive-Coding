# 3. Longest Substring Without Repeating Characters - Medium
# Tags - Hash Table, Two Pointers, String, Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        map = {}
        for j in range(n):
            if s[j] in map:
                i = max(i, map[s[j]])
            res = max(res, j - i + 1)
            map[s[j]] = j + 1
        return res
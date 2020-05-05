# 387. First Unique Character in a String - Easy
# Tags - Hash Table, String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        stringset = collections.Counter(s)
        i = 0
        for ch in s:
            if(stringset[ch] == 1):
                return i
            i += 1
        return -1
# 14. Longest Common Prefix - Easy
# Tags - String

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""
        prefix = min(strs, key=len)
        i = 0
        while prefix != "":
            for i,v in enumerate(strs):
                if(prefix not in v or v.index(prefix) != 0):
                    break
                if i == len(strs)-1:
                    return prefix
            prefix = prefix[:-1]
        return prefix
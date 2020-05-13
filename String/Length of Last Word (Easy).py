# 58. Length of Last Word - Easy
# Tags - String

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        if(res is None or (not res)):
            return 0
        else:
            return(len(res[-1]))
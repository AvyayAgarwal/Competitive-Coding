# 402. Remove K Digits - Medium
# Tags - Stack, Greedy

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k == 0):
            return num
        if(k == len(num)):
            return "0"
        res = []
        for char in num:
            while(len(res) > 0 and res[-1] > char and k > 0):
                res.pop()
                k = k - 1
            res.append(char)
        if k > 0:
            res = res[:-k]
        
        s = "".join(res).lstrip("0")
        if(s == ""):
            s = "0"
        return s
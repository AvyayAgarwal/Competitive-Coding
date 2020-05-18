# 567. Permutation in String - Medium
# Tags - Two Pointers, Sliding Window

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        if(s1len > s2len):
            return False
        
        s1map = [0] * 26
        s2map = [0] * 26
        
        for i in range(0, s1len):
            s1map[ord(s1[i]) - 97] += 1
            s2map[ord(s2[i]) - 97] += 1        
        for i in range(0, s2len - s1len):
            if(s1map == s2map):
                return True
            s2map[ord(s2[i]) - 97] -= 1
            s2map[ord(s2[i + s1len]) - 97] += 1
        return s1map == s2map
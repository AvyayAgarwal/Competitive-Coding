# 383. Ransom Note - Easy
# Tags - String

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        notemap = collections.Counter(ransomNote) # Returns dict with each char as keys with value as the frequency in the given string
        magmap = collections.Counter(magazine)
        
        for ch in notemap:
            if(ch not in magmap) or (notemap[ch] > magmap[ch]):
                return False
        return True
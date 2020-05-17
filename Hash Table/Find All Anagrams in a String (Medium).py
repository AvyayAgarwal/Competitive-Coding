# 438. Find All Anagrams in a String - Medium
# Tags - Hash Table

# Note - can be made cleaned and improved combining Hash Table with Sliding Window to make it more efficient

# Hash Table with Sliding Window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        slen = len(s)
        res = []
        pmap = collections.Counter(p)
        smap = collections.Counter(s[:plen])
        if(pmap == smap):
                res.append(0)
        for i in range(1, slen-plen+1):
            smap[s[i-1]] -= 1
            if(smap[s[i-1]] == 0):
                del smap[s[i-1]]
            smap[s[i+plen-1]] += 1
            if(pmap == smap):
                res.append(i)
        return res


# Just Hash Table
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        plen = len(p)
        slen = len(s)
        res = []
        pmap = collections.Counter(p)
        for i in range(0, slen-plen+1):
            if(pmap == collections.Counter(s[i:i+plen])):
                res.append(i)
        return res
        
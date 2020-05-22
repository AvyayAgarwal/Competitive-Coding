# 451. Sort Characters By Frequency - Medium
# Tags - Hash Table, Heap

class Solution:
    def frequencySort(self, s: str) -> str:
        smap = collections.Counter(s).most_common()
        res = ""
        for tup in smap:
            res += tup[0]*tup[1]
        return res
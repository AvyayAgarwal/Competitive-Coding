# 1207. Unique Number of Occurrences - Easy
# Tags - Hash Table

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countvals = list(collections.Counter(arr).values())
        if(len(countvals) == len(set(countvals))):
            return True
        else:
            return False
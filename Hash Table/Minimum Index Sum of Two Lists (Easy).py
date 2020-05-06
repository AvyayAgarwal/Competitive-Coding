# 599. Minimum Index Sum of Two Lists - Easy
# Tags - Hash Table

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restmap = {}
        res = []
        mindex = len(list1) + len(list2)
        for i,v in enumerate(list1):
            restmap[v] = i
        for i,v in enumerate(list2):
            if v in restmap:
                if i + restmap[v] < mindex:
                    res = [v]
                    mindex = i + restmap[v]
                elif i + restmap[v] == mindex:
                    res.append(v)
        return res
                    
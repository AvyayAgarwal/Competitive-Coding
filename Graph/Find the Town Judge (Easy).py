# 997. Find the Town Judge - Easy
# Tags - Graph

# Note - Given solution is not a formal graph solution. Can be improved and cleaned to make a proper graph solution.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if(trust is None or len(trust) == 0): return 1
        people, trustees = zip(*trust)
        pset = set(people)
        tset = set(trustees)
        res = list(tset - pset)
        print(res)
        for num in res:
            if(trustees.count(num)==N-1 and num not in pset):
                return num
        return -1
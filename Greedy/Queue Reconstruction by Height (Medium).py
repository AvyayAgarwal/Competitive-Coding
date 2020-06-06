# 406. Queue Reconstruction by Height - Medium
# Tags - Greedy

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key=lambda p: (-p[0], p[1]))
        
        for i in range(len(people)):
            res.insert(people[i][1], people[i])
        
        return res
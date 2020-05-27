# 886. Possible Bipartition - Medium
# Tags - Depth-first Search (DFS)

class Solution:        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def checker(person, color):
            colormap[person] = color
            for dis in personmap[person]:
                if (colormap[dis] == color) or (colormap[dis] == 0 and checker(dis, -color) == False):
                    return False
            return True
        
        if N == 1 or not dislikes:
            return True
        
        personmap = collections.defaultdict(list)
        colormap = [0] * (N+1)
        
        for i, j in dislikes:
            personmap[i].append(j)
            personmap[j].append(i)
                
        for person in range(1, N+1):
            if colormap[person] == 0 and checker(person, 1) == False:
                return False
            
        return True
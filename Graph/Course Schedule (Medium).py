# 207. Course Schedule - Medium
# Tags - Depth-first Search (DFS), Breadth-first Search (BFS), Graph, Topological Sort

class Solution: 
    def __init__(self):
        self.cycleFlag = False
        self.prereqGraph = collections.defaultdict(set)
        self.visitColor = []
        
    def checkSelf(self, courseNum):
            if self.cycleFlag == True or self.visitColor[courseNum] == 1:
                self.cycleFlag = True
                return
            elif self.visitColor[courseNum] == 0:
                self.visitColor[courseNum] = 1
                for adj in self.prereqGraph[courseNum]:
                    self.checkSelf(adj)
                self.visitColor[courseNum] = 2
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visitColor = [0] * numCourses
        
        for pre in prerequisites:
            self.prereqGraph[pre[0]].add(pre[1])
                
        for i in range(numCourses):
            if(self.visitColor[i] == 0):
                self.checkSelf(i)
            if self.cycleFlag == True:
                return False
        return True
# 1232. Check If It Is a Straight Line - Easy
# Tags - Array, Math, Geometry

class Solution:
    def calcSlope(self, p1: List[int], p2: List[int]):
        if(p2[0]-p1[0] == 0):
            return 0
        return (p2[1]-p1[1])/(p2[0]-p1[0])
        
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        initSlope = self.calcSlope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates), 2):
            if i+1 == len(coordinates):
                i -= 1
            if(initSlope != self.calcSlope(coordinates[i], coordinates[i+1])):
                return False
        return True
# 54. Spiral Matrix - Medium
# Tags - Array

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        if not matrix:
            return []
        
        rows = len(matrix)            
        cols = len(matrix[0])
        res = []
        
        topRow = 0
        leftCol = 0
        bottomRow = rows - 1
        rightCol = cols - 1
        
        i = 0
        j = 0
        
        while topRow <= bottomRow and leftCol <= rightCol:
            for j in range(leftCol, rightCol+1):
                res.append(matrix[topRow][j])
            topRow += 1
            
            for i in range(topRow, bottomRow+1):
                res.append(matrix[i][rightCol])
            rightCol -= 1
            
            if topRow <= bottomRow:
                for j in reversed(range(leftCol, rightCol+1)):
                    res.append(matrix[bottomRow][j])
            bottomRow -= 1
            
            if leftCol <= rightCol:
                for i in reversed(range(topRow, bottomRow+1)):
                    res.append(matrix[i][leftCol])
            leftCol += 1
            
        
        return res
            
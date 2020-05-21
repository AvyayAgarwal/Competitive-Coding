# 1277. Count Square Submatrices with All Ones - Medium
# Tags - Array, Dynamic Programming (DP)

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        res = 0
        
        for row in range(0, rowLen):
            for col in range(0, colLen):
                if matrix[row][col] == 1:
                    if row == 0 or col == 0:
                        res += 1
                    else:
                        squareMin = min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])
                        res += squareMin + matrix[row][col]
                        matrix[row][col] += squareMin
        return res
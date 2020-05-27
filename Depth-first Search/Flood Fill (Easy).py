# 733. Flood Fill - Easy
# Tags - Depth-first Search (DFS)

class Solution: 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origColor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        if origColor == newColor:
            return image
        
        def checkDir(i: int, j: int):
            if((i < 0 or j < 0 or i >= rows or j >= cols) or (image[i][j] != origColor)):
                return
            image[i][j] = newColor
            checkDir(i-1, j)
            checkDir(i+1, j)
            checkDir(i, j-1)
            checkDir(i, j+1)
            return
        checkDir(sr, sc)
        return image
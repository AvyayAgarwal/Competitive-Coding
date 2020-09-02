# 200. Number of Islands - Medium
# Tags - Depth-first Search (DFS), Breadth-first Search (BFS), Union Find

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        def dfs(matrix, row, col):
            m = len(grid)
            n = len(grid[0])
            
            if row >= m or col >= n or row < 0 or col < 0 or matrix[row][col] == '0':
                return
            grid[row][col] = '0'
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        
        return count
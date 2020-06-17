# 130. Surrounded Regions - Medium
# Tags - Depth-first Search (DFS), Breadth-first Search (BFS), Union Find

class Solution:        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfsCheck(board: List[List[str]], i: int, j: int, m: int, n: int):
            if((i >= 0 and i < m) and (j >= 0 and j < n) and (board[i][j] == "O")):
                board[i][j] = "T"
                dfsCheck(board, i, j + 1, m, n)
                dfsCheck(board, i, j - 1, m, n)
                dfsCheck(board, i + 1, j, m, n)
                dfsCheck(board, i - 1, j, m, n)
            else:
                return
        
        if board == None or len(board) == 0: return
        m = len(board)
        n = len(board[0])
        
        for i in range(n):
            if board[0][i] == "O":
                dfsCheck(board, 0, i, m, n)
            if board[-1][i] == "O":
                dfsCheck(board, m-1, i, m, n)
        
        for i in range(m):
            if board[i][0] == "O":
                dfsCheck(board, i, 0, m, n)
            if board[i][-1] == "O":
                dfsCheck(board, i, n-1, m, n)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == 'O':
                    board[i][j] = "X"
        
        return
        
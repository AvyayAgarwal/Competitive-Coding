# 133. Clone Graph - Medium
# Tags - Depth-first Search (DFS), Breadth-first Search (BFS), Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = dict()
        
        def recur(n):
            if n is None:
                return n
            if n in seen:
                return seen[n]
            
            newNode = Node(n.val)
            seen[n] = newNode
            if n.neighbors and len(n.neighbors) > 0:
                newNode.neighbors = [recur(nd) for nd in n.neighbors]
            return newNode
        
        return recur(node)
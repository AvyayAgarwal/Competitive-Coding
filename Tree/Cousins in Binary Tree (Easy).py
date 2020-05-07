# 993. Cousins in Binary Tree - Easy
# Tags - Tree, Breadth-first Search (BFS)

# Note - Regardless of the BFS tag, my code actuall runs Depth-first Search (DFS)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkDepth(self, node: TreeNode, parent: TreeNode, num: int, depth: int):
        if(node == None):
            return None
        elif node.val == num:
            return (depth, parent.val)
        else:
            right =  self.checkDepth(node.right, node, num, depth+1)
            left =  self.checkDepth(node.left, node, num, depth+1)
            if(right is None):
                return left
            else:
                return right
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:      
        xres = self.checkDepth(root, root, x, 0)
        yres = self.checkDepth(root, root, y, 0)
        if(xres != None and yres != None) and (xres[0] == yres[0] and xres[1] != yres[1]):
                return True
        else:
            return False
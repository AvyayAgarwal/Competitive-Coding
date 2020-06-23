# 222. Count Complete Tree Nodes - Medium
# Tags - Binary Search, Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = 0
        right = 0
        if root.left != None:
            left = self.countNodes(root.left)
        if root.right != None:
            right = self.countNodes(root.right)
        return 1 + left + right

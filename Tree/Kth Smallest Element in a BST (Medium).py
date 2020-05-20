# 230. Kth Smallest Element in a BST - Medium
# Tags - Binary Search, Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inTraverse(self, root: TreeNode):
        if(root is None):
            return []
        else:
            return self.inTraverse(root.left) + [root.val] + self.inTraverse(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.inTraverse(root)[k-1]
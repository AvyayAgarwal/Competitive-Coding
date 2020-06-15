# 700. Search in a Binary Search Tree - Easy
# Tags - Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        elif root.val < val and root.right != None:
            return self.searchBST(root.right, val)
        elif root.val > val and root.left != None:
            return self.searchBST(root.left, val)
        else:
            return None
# 94. Binary Tree Inorder Traversal - Medium
# Tags - Hash Table, Stack, Tree

# Note - Can be improved

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root is None):
            return None
        res = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        if(left is None and right is None):
            return res
        elif(right is None):
            left.extend(res)
            return left
        elif(left is None):
            res.extend(right)
            return res
        else:
            left.extend(res)
            left.extend(right)
            return left
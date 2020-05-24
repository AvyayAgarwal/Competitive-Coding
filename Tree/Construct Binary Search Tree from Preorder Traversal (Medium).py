# 1008. Construct Binary Search Tree from Preorder Traversal - Medium
# Tags - Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def populateChildren(self, root: TreeNode, val):
        if root == None:
            return
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.populateChildren(root.left, val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.populateChildren(root.right, val)
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.populateChildren(root, preorder[i])
        return root
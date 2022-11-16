# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node1 = p 
        node2 = q
        if root is None:
            return None
        if root == node1 or root == node2:
            return root
        left = self.lowestCommonAncestor(root.left, node1, node2)
        right = self.lowestCommonAncestor(root.right, node1, node2)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
                
        
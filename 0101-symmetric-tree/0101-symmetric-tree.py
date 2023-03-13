# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and root.right:
            return False
        if not root.right and root.left:
            return False
        def comp(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val != q.val:
                return False
            return comp(p.left, q.right) and comp(p.right, q.left)
        
        return comp(root.left, root.right)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return True
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        if not root:
            return True
        
        l = getHeight(root.left)
        r = getHeight(root.right)
        
        if abs(l-r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
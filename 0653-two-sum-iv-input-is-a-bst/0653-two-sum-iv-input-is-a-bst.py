# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l1 = []
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            l1.append(root.val)
            inorder(root.right)
        inorder(root)
        
        l = 0 
        r = len(l1)-1
        
        while l < r:
            s = l1[l] + l1[r]
            if s == k:
                return True
            elif s < k:
                l+=1 
            else:
                r-=1
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.count = 1
        
        def dfs(root):
            if not root:
                return
            if self.ans:
                return 
            dfs(root.left)
            if self.ans == None and self.count == k:
                self.ans = root.val
                return
            self.count += 1
            dfs(root.right)
        
        dfs(root)
        return self.ans
                
        
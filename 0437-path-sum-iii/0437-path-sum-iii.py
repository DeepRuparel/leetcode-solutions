# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        
        def dfs2(root, target):
            if not root:
                return 
            if root.val == target:
                self.ans += 1
            dfs2(root.left, target - root.val)
            dfs2(root.right, target - root.val)
    
        def dfs(root):
            if not root:
                return 
            dfs2(root, targetSum)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.ans
        
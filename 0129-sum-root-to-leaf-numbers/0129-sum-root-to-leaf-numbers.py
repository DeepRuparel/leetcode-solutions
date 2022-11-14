# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        numbers = []
        
        def dfs(root, current_sum):
            if not root:
                return 
            current_sum += str(root.val)
            if not root.left and not root.right:
                numbers.append(current_sum)
            if root.left:
                dfs(root.left, current_sum)
            if root.right:
                dfs(root.right, current_sum)
            
        dfs(root, "")
        ans = 0
        for i in numbers:
            ans += int(i)
        return ans
        
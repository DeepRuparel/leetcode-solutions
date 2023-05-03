# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            
            withroot = root.val + left[1] + right[1]
            withoutroot = max(left) + max(right)
            
            return [withroot, withoutroot]
        return max(dfs(root))
                
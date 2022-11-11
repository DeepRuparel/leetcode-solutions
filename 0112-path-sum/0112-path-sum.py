# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global flag
        flag = False
        
        def check(root, c_sum):
            global flag 
            
            if not root:
                return 0
            c_sum += root.val
            
            if not root.left and not root.right:
                if c_sum == targetSum:
                    flag = True
                    return 
            check(root.left, c_sum)
            check(root.right, c_sum)
        check(root, 0)
        return flag
            
                    
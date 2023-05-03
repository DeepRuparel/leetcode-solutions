# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getheight(root):
            if not root:
                return 0
            return 1 + getheight(root.left)
        if not root:
            return 0
        lefth = getheight(root.left)
        righth = getheight(root.right)
        
        if lefth == righth:
            return (2 ** lefth) + self.countNodes(root.right)
        else:
            return (2 ** righth) + self.countNodes(root.left)
        
        
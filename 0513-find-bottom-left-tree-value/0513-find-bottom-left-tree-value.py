# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        val = -1
        if not root:
            return val
        q = deque([root])
        
        while q:
            first = True
            for i in range(len(q)):
                node = q.popleft()
                if first:
                    val = node.val
                    first = False
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return val
                
        
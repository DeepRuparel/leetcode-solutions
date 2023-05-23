# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = float("-inf")
        q = deque([root])
        hlevel = 0
        level = 1
        if root.val > ans:
            ans = root.val
            hlevel = level
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if q:
                s = 0
                for i in q:
                    s += i.val
                if s > ans:
                    ans = s
                    hlevel = level
        return hlevel
            
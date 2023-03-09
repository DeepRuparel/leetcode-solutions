# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # edge case if no root
        if not root:
            return []
        
        #do a bfs because it is inyuitive
        
        q = deque([root])
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                n = q.popleft()
                temp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ans.append(temp)
        return ans
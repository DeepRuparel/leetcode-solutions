# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        level = 1
        q = deque([(root, level)])
        
        while q:
            for _ in range(len(q)):
                node, level = q.popleft()
                if q and level < q[0][1]:
                    ans.append(node.val)
                if not q:
                    ans.append(node.val)
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
                level += 1
        return ans
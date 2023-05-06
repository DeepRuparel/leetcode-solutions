# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        
        ans = float("inf")
        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) < ans:
                ans = abs(arr[i] - arr[i + 1])
        return ans
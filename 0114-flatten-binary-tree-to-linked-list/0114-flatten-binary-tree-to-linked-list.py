# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        arr = []
        def inorder(root):
            if not root:
                return
            arr.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        i = 1
        while i < len(arr):
            root.left = None
            root.right = TreeNode(arr[i])
            i+= 1
            root = root.right
        
        
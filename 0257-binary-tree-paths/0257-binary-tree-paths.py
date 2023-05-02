# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        def dfs(root, curr_path):
            if not root:
                return
            curr_path += str(root.val)+"->"
            if not root.left and not root.right:
                paths.append(curr_path)
            
            if root.left:
                dfs(root.left, curr_path)
            if root.right:
                dfs(root.right, curr_path)
            
        dfs(root, "")
        #print(paths)
        ans  = []
        for i in paths:
            ans.append(i[:-2])
        print(ans)
        return ans
        return []
        
            
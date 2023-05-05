'''
do a dfs approach maybe 
and do like a swap using a third variable temp
    4
   / \
  2.  7
 / \. / \
1  3 6   9

root = 4
temp = root.left
temp =  2
       / \
       1   3
root.left = root.right
root.left =   7
            /   \
          9      6
root.right = temp
root.right =  2
             / \
            1   3
tree now is 

        4
      /   \
      7    2
    /   \  / \
  9      6 1   3
 do the same for all nodes
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root
        
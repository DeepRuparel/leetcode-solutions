
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
        4
       / \
      2.  6
     / \ 
     1  3
inroder travesal
1, 2, 3, 4, 6
                  1    1    1   1
distance = [inf, inf, inf, inf, inf]
1, 2, 3, 4, 5, 6
    ^ 
             ^
compare 2 with 1 and 3 difference is 1 update distance 
 3 - 2 = 1
 4 - 3  = 1
 5 - 4  = 1
 6 - 5 = 1
 min(distance) = 1
 
 ########## optimization #############
 use a single min distance instead of array
'''
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sortedarray = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            sortedarray.append(root.val)
            inorder(root.right)
        # call inorder to get an sorted array
        inorder(root)
        distance = [float("inf")] * len(sortedarray)
        for i in range(1, len(distance)):
            distance[i] = min(distance[i], sortedarray[i] - sortedarray[i-1])
        
        return min(distance)
            
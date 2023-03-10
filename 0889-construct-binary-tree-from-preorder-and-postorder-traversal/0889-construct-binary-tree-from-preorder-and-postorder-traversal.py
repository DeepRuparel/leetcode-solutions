# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
1, 2, 4, 5, 3, 6, 7
4, 5, 2, 6, 7, 3, 1

last of node always the root of the tree
pop it out find the index of the last of psot which is 3
every thing from 1 to index of 3 in pre is in left of node
and everthing from index to end is in right of node
        1
    
    /       \
    2,4,5   3,6,7
            3
           / \
           6   7
           
#hint : construc the right hand size first
'''
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def createTree(pre, post):
            
            #base condition
            if not pre:
                return
            if len(pre) == 1:
                return TreeNode(post.pop())
            
            root = TreeNode(post.pop())
            preIndex = pre.index(post[-1])
            
            root.right = createTree(pre[preIndex:], post)
            root.left = createTree(pre[1:preIndex], post)
            return root
        return createTree(preorder, postorder)
            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Iterative solution 

        3
     /      \
     5      1
    /  \    / \
    6   2   0   8
        /\
        7 4
keep adding in dictionary the current node.left and right with their parents until we find 5 and 4
do a bfs
so dictionary {root: None, 5:3, 1:3, 0:1, 8:1, 6:5, 2:5, 7:2, 4:2}
ancestors of p = (5 -> 3)
search for q in ancestors
q = 4
4 -> 2 -> 5 
5 in ancestors 
so return 5
parent root : None
do bfs until we find both p and q in the parents dictionary

one we have both the p and q in dictionary

make a set of ancestors and put all the ancstors of p in it

now ntil q is found in that ancestor we keep looking in it

return q
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        parents = {root:None}
        
        while p not in parents or q not in parents:
            node = queue.pop()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
        
        ancestors_of_p = set()
        
        while p:
            ancestors_of_p.add(p)
            p = parents[p]
        
        #search q in ancestors
        while q not in ancestors_of_p:
            q = parents[q]
        return q
                
        
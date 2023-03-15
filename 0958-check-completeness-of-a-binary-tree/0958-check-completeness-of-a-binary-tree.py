# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
approach do a bfs to get nodes at each level
store them in an array
if array.size() != 2^h and check if it is the last level
and if i see a missing child in the end I can append a '#' in the middle rather then the end 
i return false
meaning not all nodes are at the same level

'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            q = deque([root])
            h = 0
            while q:
                for i in range(len(q)):
                    n = q.popleft()
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                h+=1
            return h
        if not root:
            return False
        h = height(root)
        
        curr_h = 1
        q = deque([root])
        if len(q) > h:
            return False
        if len(q) == h:
            return True
        while curr_h != h:
            temp = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    temp.append(node.left.val)
                else:
                    temp.append('#')
                if node.right:
                    q.append(node.right)
                    temp.append(node.right.val)
                else:
                    temp.append('#')
            #print(temp, curr_h)
            if len(q) == 2 ** curr_h:
                curr_h += 1
                continue
            else:
                if curr_h == h - 1:
                    k = 0
                    for i in range(len(temp)):
                        if temp[i] == '#':
                            k = i
                            break
                    #print(k)
                    for i in range(k+1, len(temp)):
                        if temp[i] != '#':
                            return False
                    return True
                else:
                    return False
                curr_h += 1
            
        return True
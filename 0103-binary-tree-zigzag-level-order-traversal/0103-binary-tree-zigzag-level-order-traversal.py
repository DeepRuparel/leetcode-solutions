'''
since we want all the leaves at the same level we have to bfs
also add a varibale when even doesnpt reverse the list andd when odd reverses the list and appends it to ans
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #base condition for emptty root
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        isEven = 0
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                #check if right and left and append them to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if isEven % 2 == 1:
                temp = temp[::-1]
            isEven += 1
            ans.append(temp)
        return ans
            
        
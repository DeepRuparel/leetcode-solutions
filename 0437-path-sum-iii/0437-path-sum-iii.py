# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right]
'''
Brute force approach:
flatten the bionary tree from each node and use loops to acquire the targetSum

We need dfs because tree
            10
           /  \
          5     -3
         / \    / \
        3   2       11
       / \   \
      3  -2   1

root = 10
add to list [10]
root.left 5 [10+5]
root.left 3 [10+5+3]
root.left 3 [10+5+3]

traditional dfs from root only because I can see 5,3 is 8 but since dfs alwats starts from root I miss the solution

Idea: Use two dfs approach 

root = 10
explore from 10 all the possible solution
now from 5
5 + roo.left. (3) == 8 add to answer
5 + root.right + root.right = 5 + 2 + 1 = 8

root = 3
nothing
root = 3 nothing
root = -2
nothing
root = 2
nothing root = 1 nothing

now root = -3 which is right of 10
-3+ 11 = 8 ans ++
root = 11 nothing

    
'''
"""
Previous solution:
 self.ans = 0
        # second dfs to calculate if sum of of path from given root is targetSum
        def dfs2(root, t):
            #base condition
            if not root:
                return
            if root.val == t:
                self.ans += 1
            dfs2(root.left, t - root.val)
            dfs2(root.right, t - root.val)
        #the outer dfs to traverse all the nodes since path doesnot need to start from root till leaf
        def dfs(root):
            #base condition
            if not root:
                return
            dfs2(root, targetSum)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans
"""
"""
saw an optimization approach in discussion:
we are calculating 10, 10 + 5, 10 + 5 + 3 , 5 +3 , 5 + 3 + 2, but we could use the 10 + 5 + 3 to get 5 + 3
by storing results in cache.

Dry run:
cache = {0, 1}
res = 0
            10
           /  \
          5     -3
         / \    / \
        3   2       11
       / \   \
      3  -2   1

cps = 0 
root = 10
cps = 0 + 10
ops = cps - target = 10 - 8 = 2
check if 2 resent in cache no res = 0 + 0
cache [0: 1, 10 : 1]
root = root.left = 5
cps = 10 + 5 = 15
ops = 15 - 8 = 7
check if 7 in cache ?
cache = [0:1, 10: 1, 15: 1]
root = root.left = 3
cps = 15 + 3 = 18
ops = 18 - 8 = 10
check if 10 in cache yes res = 0 + freq(10) = 1
cache = [0:1, 10: 1, 15: 1, 18 : 1]
root = 3
cps = 21
ops = 21 - 8 = 14
check if 14 in cache?
cache = [0:1, 10: 1, 15: 1, 18 : 1, 21 : 1] 
none and none so root.right of 3 which is -2 
root = root.right = -2
cps = 21 - 2 = 19
ops = 19 - 8 = 11
check if 11 in cache?
cache = [0:1, 10: 1, 15: 1, 18 : 1, 21: 1, 19 : 1]
cache = [0:1, 10: 1, 15: 1]
now root = 2
similarly for right of 2

"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {0: 1}
        self.result = 0
        
        self.dfs(root, targetSum, 0, cache)
        return self.result
    def dfs(self, root, target, currpathSum, cache):
            if not root:
                return
            currpathSum += root.val
            oldpathSum = currpathSum - target
            self.result += cache.get(oldpathSum, 0) 
            cache[currpathSum] = cache.get(currpathSum, 0) + 1
            
            self.dfs(root.left, target, currpathSum, cache)
            self.dfs(root.right, target, currpathSum, cache)
            
            cache[currpathSum] -= 1
        
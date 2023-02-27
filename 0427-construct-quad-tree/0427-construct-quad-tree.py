"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isSame(x1, y1, length):
            for i in range(x1, x1+length):
                for j in range(y1, y1+length):
                    if grid[i][j] != grid[x1][y1]:
                        return False
            return True
        def solve(x1, y1, length):
            #chceck if all the lements are the same
            if isSame(x1, y1, length): 
                return Node(grid[x1][y1] == 1, True, None, None, None, None)
            
            #if not same make root as current node and the four children will be x1,y1, x1,y1+4, x1+4,y1 and x1+4 and y1+4
            else:
                root = Node(False, False, solve(x1, y1,length // 2), solve(x1, y1 + length // 2, length // 2), solve(x1+length //2, y1, length // 2), solve(x1 + length // 2, y1 + length // 2, length // 2))
                return root
            
        return solve(0, 0, len(grid))
            
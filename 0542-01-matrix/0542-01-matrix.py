from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = '#'
        
        while q:
            r, c = q.popleft()
            for i, j in directions:
                row = r+i
                col = c+j
                if 0 <= row < rows and 0 <= col < cols and mat[row][col] == '#':
                    mat[row][col] = mat[r][c] + 1
                    q.append((row,col))
        
        return mat
                
                
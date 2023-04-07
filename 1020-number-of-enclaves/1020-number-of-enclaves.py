
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        
        visited = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(False)
            visited.append(temp)
                
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]  or grid[x][y] == 0:
                return 
            visited[x][y] = True
            # maek visisted as true
            # create a list of all possibl;e directions
            directionsx = [0, 1, 0, -1]
            directionsy = [-1, 0, 1, 0]
            
            for i in range(4):
                dfs(x + directionsx[i], y + directionsy[i])
            return
        # checking first column and last column
        for i in range(m):
            if grid[i][0] == 1 and visited[i][0] == False:
                dfs(i , 0)
            
            if grid[i][n-1] == 1 and visited[i][n-1] == False:
                dfs(i, n-1)
        # checking first and last row
        for i in range(n):
            if grid[0][i] == 1 and visited[0][i] == False:
                dfs(0, i)
            if grid[m-1][i] == 1 and visited[m-1][i] == False:
                dfs(m-1, i)
        # answer to store asnwers
        ans = 0
        # iterate to see which 1 ares not visted since they are the answer
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    ans += 1
        return ans
                
                
                
                
                
                
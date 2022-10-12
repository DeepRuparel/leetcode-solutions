class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        island = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    island += 1
        return island
    
    def dfs(self,grid,r,c):
        row = len(grid)
        column = len(grid[0])
        
        if r < 0 or r >= row or c < 0 or c >= column:
            return 
        if grid[r][c] == '0':
            return 
        grid[r][c] = '0'
        self.dfs(grid,r+1,c)
        self.dfs(grid,r-1,c)
        self.dfs(grid,r,c+1)
        self.dfs(grid,r,c-1)
        
                    
        
        
        
        
        
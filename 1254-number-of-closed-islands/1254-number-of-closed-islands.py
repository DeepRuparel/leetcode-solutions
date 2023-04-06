class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(row, col):
            if (row in (0, ROWS - 1) or col in (0, COLS - 1)) and grid[row][col] == 0:
                return False
        
            if grid[row][col] == 1 or (row, col) in visited:
                return True
            
            visited.add((row, col))
            
            top = dfs(row - 1, col)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)
            return top and bottom and left and right
        
        closedIslands = 0
        for row in range(1, ROWS - 1):
            for col in range(1, COLS - 1):
                if grid[row][col] == 0 and (row, col) not in visited:
                    closedIslands += dfs(row, col)
        return closedIslands
        
        
                
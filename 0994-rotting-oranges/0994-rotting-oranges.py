class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append([i,j])
        time = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                a,b = queue.popleft()
                for i,j in [[a,b-1],[a,b+1],[a-1,b],[a+1,b]]:
                    if i >= len(grid) or i < 0 or j < 0 or j>= len(grid[0]) or grid[i][j]!=1:
                        continue
                    grid[i][j] = 2
                    queue.append([i,j])
                    
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                    
                    
                    
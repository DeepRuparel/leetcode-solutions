class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] or grid[n-1][n-1]:
            
            return -1
        q = deque([(0, 0, 1)])
        # start, dest , cost
        visited = set()
        visited.add((0,0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1,1), (-1, -1)]
        while q:
            x, y, steps = q.popleft()
            if x == n - 1 and y == m - 1:
                return steps
            for nx, ny in dirs:
                nx += x
                ny += y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != 1:
                    visited.add((nx,ny))
                    q.append((nx, ny, steps + 1))
        return -1
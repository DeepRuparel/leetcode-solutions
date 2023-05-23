class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        same = 0
        for i in range(len(grid)):
            s = str(grid[i])
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            temp = str(temp)
            if temp in d:
                same += d[temp]
        return same
                
        
        
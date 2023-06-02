class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                if i == j:
                    continue
                
                if r1 **2 >= (x1-x2)**2 + (y1-y2) ** 2:
                    adjlist[i].append(j)
        maxbombs = 0
        def dfs(currbomb, visited):
            if currbomb in visited:
                return 
            visited.add(currbomb)
            
            for nei in adjlist[currbomb]:
                if nei not in visited:
                    dfs(nei, visited)
            return visited
                    
            
        for i in range(n):
            visited = set()
            visited = dfs(i, visited)
            #print(visited, i)
            maxbombs = max(maxbombs, len(visited))
        return maxbombs
        
        
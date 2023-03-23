class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n - 1:
            return -1 
        adjlist = defaultdict(list)
        
        for src, dest in connections:
            adjlist[src].append(dest)
            adjlist[dest].append(src)
        
        
        
        visited = set()
        numberofconnected = 0
        
        def dfs(i):
            visited.add(i)
            for j in adjlist[i]:
                if j not in visited:
                    dfs(j)
        for i in range(n):
            if i not in visited:
                numberofconnected += 1
                dfs(i)
        
        return numberofconnected - 1
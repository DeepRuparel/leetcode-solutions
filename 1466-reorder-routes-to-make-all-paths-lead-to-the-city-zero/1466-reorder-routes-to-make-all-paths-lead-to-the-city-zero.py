class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adjlist = defaultdict(list)
        for i, j in connections:
            adjlist[i].append([j, 1])
            adjlist[j].append([i, -1])
        
        visited = set()
        self.count = 0
        def dfs(start):
            visited.add(start)
            for nei, way in adjlist[start]:
                if nei not in visited:
                    if way == 1:
                        self.count += 1
                    dfs(nei)
        dfs(0)
        return self.count
                        
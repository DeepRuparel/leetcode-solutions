class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        if source == destination:
            return True
        for s,d in edges:
            adjlist[s].append(d)
            adjlist[d].append(s)
        if source not in adjlist or destination not in adjlist:
            return False
        q = deque([source])
        visited = set()
        while q:
            node = q.popleft()
            if node == destination:
                return True
            visited.add(node)
            for nei in adjlist[node]:
                if nei not in visited:
                    q.append(nei)
        return False
                
        
        
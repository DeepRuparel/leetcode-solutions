class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(set)
        
        def dfs(src, dest):
            if src not in seen:
                seen.add(src)
                if src == dest:
                    return True
                return any(dfs(neighbor, dest) for neighbor in graph[src])

        
        for source, dest in edges:
            seen = set()
            
            if source in graph and dest in graph and dfs(source,dest):
                return source, dest
            graph[source].add(dest)
            graph[dest].add(source)
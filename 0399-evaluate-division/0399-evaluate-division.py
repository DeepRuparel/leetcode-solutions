class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def bfs(src,dest,value):
            visited = set()
            queue = [[src,value]]
            
            while queue:
                node, val = queue.pop(0)
                if node == dest:
                    return val
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        new_val = val* graph[node][neighbor]
                        queue.append([neighbor,new_val])
            return (float(-1))
            
        
        #create a graph with reverse and orignal values
        graph = {}
        for i in range(len(values)):
            src,dest = equations[i]
            val = values[i]
            rev = 1 / val
            if src in graph:
                graph[src][dest] = val
            else:
                graph[src] = {dest:val}
            if dest in graph:
                graph[dest][src] = rev
            else:
                graph[dest] = {src: rev}
        
        res = []
        for src, dest in queries:
            if src not in graph or dest not in graph:
                res.append(float(-1))
            else:
                res.append(bfs(src,dest,1))
        return res
            
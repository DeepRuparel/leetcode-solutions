class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjlist = defaultdict(list)
        i = 0
        for s,d in edges:
            adjlist[s].append((d, succProb[i]))
            adjlist[d].append((s, succProb[i]))
            i += 1
        
        h = []
        heapq.heappush(h, [-1, start])
        values = [0.0] * n
        values[start] = 1.0
        visited = set()
        if start == end:
            return values[start]
        while h:
            #print(h)
            cost, node = heapq.heappop(h)
            visited.add(node)
            for nei, nei_cost in adjlist[node]:
                if nei not in visited:
                    if nei_cost * -cost > values[nei]:
                        values[nei] = nei_cost * -cost
                        heapq.heappush(h, (nei_cost * cost, nei))
        if values[end] == -1:
            return float(0)
        return float(values[end])
                
                
            
        return 0.25000
        
            
        
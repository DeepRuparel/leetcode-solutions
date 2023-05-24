class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        q =[]
        ans = []
        heapq.heappush(q, [0, [0]])
        n = len(graph)
        dest = n - 1
        
        while q:
            node, path = heapq.heappop(q)
            if node == dest:
                ans.append(path)
            for nei in graph[node]:
                heapq.heappush(q, [nei, path + [nei]])
        
        return ans
        
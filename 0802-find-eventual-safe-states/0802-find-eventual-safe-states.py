class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = defaultdict(list)
        outdegree = defaultdict(int)
        queue = []
        res = []
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            if outdegree[i] == 0:
                queue.append(i)
            
            for j in graph[i]:
                indegree[j].append(i)
        #print(indegree)
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            for innode in indegree[node]:
                outdegree[innode] -= 1
                if outdegree[innode] == 0:
                    queue.append(innode)
        return sorted(res)
            
        
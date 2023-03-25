class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist = defaultdict(list)
        for s,d in edges:
            adjlist[s].append(d)
            adjlist[d].append(s)
        
        unvisited = []
        visited = set()
        total = 0
        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            res = 1
            for nei in adjlist[i]:
                res += dfs(nei)
            return res
        for i in range(n):
            temp = dfs(i)
            if temp != 0:
                total += temp
                unvisited.append(temp)
        
        ans = 0
        for i in unvisited:
            ans += (total - i) * i
        return ans// 2
            
        #passed 51/66 test case until reaching tle
#         adjlist = defaultdict(list)
#         edge = set()
#         for s,d in edges:
#             adjlist[s].append(d)
#             adjlist[d].append(s)
#         nodesprocessed = set()
#         ans = set()
#         for i in range(n):
#             edge.add(i)
        
#         def dfs(node, visited):
#             if node not in visited:
#                 visited.add(node)
#                 for i in adjlist[node]:
#                     dfs(i, visited)
#             return visited
#         for i in range(0, n):
#             visited = set()
#             visited.add(i)
#             for nei in adjlist[i]:
#                 visited = dfs(nei, visited)
#             nodesprocessed.add(i)
#             #visited.remove(i)
#             #print(visited)
            
#             for node in edge:
#                 if node not in visited and (i, node) not in ans and (node, i) not in ans:
#                     ans.add((i, node))
#             # print(ans)
#             # print(len(ans))
#         #print(len(ans))
        
#         return len(ans)
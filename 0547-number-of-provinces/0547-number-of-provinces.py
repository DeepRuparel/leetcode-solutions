class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for n in adjList[node]:
                if n not in visited:
                    dfs(n)
        adjList = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and i!=j:
                    adjList[i+1].append(j+1)
        visited = set()
        
        ans = 0
        for i in range(1,len(isConnected)+1):
            if i not in visited:
                ans+=1 
                dfs(i)
        return ans
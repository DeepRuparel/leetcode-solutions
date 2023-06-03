from collections import deque
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        costs = [float("inf")] * V
        #print(cost)
        visited = set()
        
        q = deque([(S, 0)])
        visited.add(S)
        costs[S] = 0
        
        while q:
            node, cost = q.popleft()
            
            for nei, neicost in adj[node]:
                newcost = cost + neicost
                if costs[nei] > newcost:
                    costs[nei] = newcost
                    q.append((nei, newcost))
                    visited.add(nei)
        #print(costs)
        return costs
                    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
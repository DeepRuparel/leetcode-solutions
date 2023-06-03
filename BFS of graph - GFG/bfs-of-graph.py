#User function Template for python3

from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code 
        q = deque([0])
        visited = set()
        ans = []
        visited.add(0)
        ans.append(0)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                #visited.add(node)
                #.append(node)
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        ans.append(nei)
                        q.append(nei)
        return ans
        


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
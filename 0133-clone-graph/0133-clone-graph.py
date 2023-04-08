"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # a dictionary to store the graph
        newgraph = {}
        
        # do a dfs on all the nodes
        def dfs(node):
            # if node already in new so no need to explore it
            if node in newgraph:
                return newgraph[node]
            
            # if not in new
            # create a copy of node
            
            copy = Node(node.val)
            newgraph[node] = copy
            
            # add all the neighors of node to copy  node and do a dfs on it
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        if node:
            return dfs(node)
        else:
            return None
#         oldToNew = {}
        
#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]
            
#             copy = Node(node.val)
#             oldToNew[node] = copy
            
#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei))
#             return  copy       
        
#         if node:
#             return dfs(node)
#         else:
#             return None
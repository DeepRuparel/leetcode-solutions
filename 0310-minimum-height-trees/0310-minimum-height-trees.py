class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        neighbors = defaultdict(set)
        # creating a dictionary of edges
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)
        
        leaves = []
        for i in range(n):
            # checking if there is only one edge meaning it is a leaf edge
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        # pruning the tree to reach the centroid
        
        reaminingnodes = n
        
        while reaminingnodes > 2:
            #print(reaminingnodes)
            reaminingnodes -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                # pop the only neighbor for the leaf node
                neighbor = neighbors[leaf].pop()
                # removing the edge from the neighbors set
                neighbors[neighbor].remove(leaf)
                # checking after pruning is there only one edge left
                # if yes adding it to new leaves
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
                
            
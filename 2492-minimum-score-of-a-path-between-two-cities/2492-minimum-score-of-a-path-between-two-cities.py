class Solution:
    '''
          1
        4/  \ 2
        3   2
      7 |
        4
        
create a adj list so 
1 [2,2] [3,4]
2 [1,2]
3 [1,4] [4, 7]
4 [3, 7]

do a bfs so
append to q because we know starting point is 1
cost = inf
visited = []

q = [1]

pop out q
n = 1
add to visited 1

append children of 1 to q 
check if children node in visited if not append so q [2,3]
check if the current cost is min then 
2 < inf
so cost = 2
4 < 2 ? no donot chnage

q = [2,3]
n = 2
neend not append anything because 1 already appended

visited = [1,2]
n = 3
add to viisted
append children of 3 which are 4
q = [4]
visisted = [1,2,3]
cost is 7 7 < 2? nope donot touch

q = []
n = 4
chikldren alreadyu in iisted donot do anything

q is empty exit 
return cost
'''
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        adjlist = defaultdict(dict)
        for u, v, w in roads:
            adjlist[u][v] = adjlist[v][u] = w
        cost = inf
        q = deque([1])
        visisted = set()
        while q: 
            node = q.popleft()
            for adj, c in adjlist[node].items():
                if adj not in visisted:
                    q.append(adj)
                    
                    visisted.add(adj)
                cost = min(c, cost)
        return cost
                      
        
        
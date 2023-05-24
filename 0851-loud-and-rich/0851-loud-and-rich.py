class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adjlist = defaultdict(list)
        
        for r,p in richer:
            adjlist[p].append(r)
            
        #print(adjlist)
        
        res = [x for x in range(len(quiet))]
        #print(adjlist)
        for i in range(len(quiet)):
            visited = set()
            q = deque([(i, quiet[i])])
            globalcurrlevel = quiet[i]
            while q:
                node, curr_level = q.popleft()
                visited.add(node)
                for nei in adjlist[node]:
                    if nei not in visited:
                        #print(quiet[nei], curr_level, node, nei)

                        if quiet[nei] < globalcurrlevel:
                            globalcurrlevel = quiet[nei]
                            res[i] = nei
                            #print(res)
                        q.append([nei, curr_level])
        #print(res)
        
        return res
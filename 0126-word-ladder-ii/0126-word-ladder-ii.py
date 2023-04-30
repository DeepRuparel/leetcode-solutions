class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # make a dictionary of words like befor with * as wildcard
        wordDict = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                wordDict[word[:i]+"*"+word[i+1:]].append(word)
        
        # now instead of soing a bfs which gives a TLE why don't we use bfs to create a adjList such that the key is the word we can reach using the children
        # so a: [b,c] using b or c we can reach a
        
        inv_adj_list = {beginWord:[]}
        found = False
        
        queue = deque([beginWord])
        
        
        while queue and not found:
            n = len(queue)
            visited_this_level = {}
            
            for _ in range(n):
                word = queue.popleft()
                for i in range(len(word)):
                    for nei in wordDict[word[:i]+"*"+word[i+1:]]:
                        if nei == endWord:
                             #we don't return immediately because other
                            # sequences might reach the endWord in the same
                            # BFS level
                            found = True
                        if nei not in inv_adj_list:
                            if nei not in visited_this_level:
                                visited_this_level[nei] = [word]
                                queue.append(nei)
                            else:
                                visited_this_level[nei].append(word)
            inv_adj_list.update(visited_this_level)
        #print(inv_adj_list)
        
        # now do a dfs to get the path from the endword to help prevent going to unwanted words
        
        def dfs(node):
            if node == beginWord:
                return [[beginWord]]
            if node not in inv_adj_list:
                return []
            res = []
            parents = inv_adj_list[node]
            for p in parents:
                res += dfs(p)
            for r in res:
                r.append(node)
            return res
        return dfs(endWord)
        
            
        
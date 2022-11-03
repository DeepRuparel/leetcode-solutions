class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        # Build an adjacency list - graph
        for emails in accounts:
            for i in range(2,len(emails)):
                adj[emails[i]].append(emails[i-1])
                adj[emails[i-1]].append(emails[i])
        
        def dfs(email):
            seen.add(email)
            res = [email]
            small = []
            
            for i in adj[email]:
                if i not in seen:
                    small += (dfs(i))
            return res + small
        
        
        
        
        seen = set()
        ans = []
        for email in (accounts):
            if email[1] not in seen:
                ans.append([email[0]] + sorted(dfs(email[1])))
        return ans
            
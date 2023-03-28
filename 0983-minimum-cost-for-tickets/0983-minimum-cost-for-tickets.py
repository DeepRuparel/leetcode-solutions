class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # three ways to select how to get the total cost
        
        '''if i is in dataset we can just return minimum(cost for all the other days + cost[0]
                                                        OR
                                                        cost for all the days starting from current day + 7 dats and cost[7]
                                                        OR 
                                                        cost for all the days starting from current day + 30 and cost[31 days]
            )
            
            anthing else we just increment the next day
        '''
        
        i = 0
        
        day = set(days)
        gaps = [1, 7, 30]
        
        '''
        was goin for a while loop but realised I need to know the values before hand making a decision
        then I can get min of it so recursively call func
        '''
        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in day:
                ans = []
                for j in range(len(gaps)):
                    ans.append(dp(i+gaps[j]) + costs[j])
                return min(ans)
            else:
                return dp(i+1)
        return dp(1)
                    
        
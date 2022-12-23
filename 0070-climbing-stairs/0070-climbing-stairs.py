class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1]*(n+1)
        #print(ans)
        for i in range(n-2,-1,-1):
            ans[i] = ans[i+1]+ans[i+2]
        
        return ans[0]
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1] * (n+1)
        
        for i in range(n-2, -1, -1):
            ans[i] = ans[i+1] + ans[i+2]
        return ans[0]
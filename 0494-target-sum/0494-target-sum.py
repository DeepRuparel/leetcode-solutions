class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i = 0 , total = 0):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            key = (i,total)
            if key not in dp:
                dp[key] = backtrack(i+1,total+nums[i]) + backtrack(i+1, total-nums[i])
            #print(dp)
            return dp[key]
        return backtrack()
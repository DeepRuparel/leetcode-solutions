class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0 
        j = 0 
        sum1 = 0 
        ans = float("inf")
        while j < len(nums):
            sum1 += nums[j]
            if sum1 < target:
                j += 1
            elif sum1 >= target:
                while sum1 >= target:

                    ans = min(ans, j-i+1)

                    sum1 -= nums[i]

                    i += 1
                j += 1 
        if ans == float("inf"):
            return 0
        else:
            return ans
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        ans = 0
        p_sum = 0
        
        for i in range(len(nums)):
            p_sum += nums[i]
            ans = max(ans, math.ceil(p_sum / (i+1)))
        return ans
            
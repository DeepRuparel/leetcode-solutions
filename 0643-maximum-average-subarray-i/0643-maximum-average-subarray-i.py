class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        
        ans = s/k
        left = 0
        for right in range(k, len(nums)):
            s = s - nums[left] + nums[right]
            ans = max(ans, s/k)
            left += 1
        return ans
            
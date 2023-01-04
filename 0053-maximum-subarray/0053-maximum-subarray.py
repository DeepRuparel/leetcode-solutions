class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1 = max2 = nums[0]
        for i in range(1,len(nums)):
            max1 = max(nums[i], max1+nums[i])
            max2 = max(max1, max2)
        return max2
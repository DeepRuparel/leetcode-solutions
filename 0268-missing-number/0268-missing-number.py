class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rangesum = sum(range(len(nums)+1))
        ans = rangesum - sum(nums)
        return ans
        
        
    
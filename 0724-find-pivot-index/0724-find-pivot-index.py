class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        fsum = sum(nums)
        
        for i in range(len(nums)):
            if lsum == fsum - nums[i]:
                return i
            lsum += nums[i]
            fsum -= nums[i]
        return -1
        
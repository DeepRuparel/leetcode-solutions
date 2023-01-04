class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        dpmin = [0]*n
        dpmax = [0]*n
        
        dpmin[0]=dpmax[0]=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] > 0:
                dpmin[i] = min(dpmin[i-1]*nums[i], nums[i])
                dpmax[i] = max(dpmax[i-1]*nums[i], nums[i])
            else:
                dpmin[i] = min(dpmax[i-1]*nums[i], nums[i])
                dpmax[i] = max(dpmin[i-1]*nums[i], nums[i])
        return max(dpmax)
            
            
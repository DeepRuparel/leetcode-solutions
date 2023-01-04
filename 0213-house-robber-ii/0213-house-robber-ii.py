class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return max(nums)
        a = 0
        b = 0
        for i in nums[:-1]:
            temp = a
            a = max(a,b+i)
            b = temp
        c,d = 0,0
        for i in nums[1:]:
            temp = c
            c = max(c, d+i)
            d = temp
        
        return max(a,c)
        
        
        
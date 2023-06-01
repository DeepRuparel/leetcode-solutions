class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums[0] == 1:
            cons = 1
        else:
            cons = 0
        m = cons
        for i in range(1, len(nums)):
            if nums[i] == 1:
                cons += 1
            else:
                cons = 0
            m = max(m, cons)
        return m
            
        
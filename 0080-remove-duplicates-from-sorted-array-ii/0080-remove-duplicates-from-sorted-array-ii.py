class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        0, 0, 1,1, 1, 1, 2, 2, 3
        pos = 1
        0 == 1 ? No
        nums[1] = 0
        pos = 2
        0 == 1?
        nums[2] = 1
        1 == 1 yes 
        1 == 1 yes
        1 == 2
        nums[3] = 1
        pos = 4 
        1 == 2
        nums[4] = 2
        pos = 5
        2 == 3
        
        '''
        if len(nums) < 3:
            return len(nums)
        pos = 1
        for i in range(1, len(nums) - 1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1
                
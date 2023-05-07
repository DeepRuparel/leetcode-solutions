class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                start = i
                break
        if start == -1:
            return nums
        for j in range(start+1, len(nums)):
            if nums[j] != 0:
                nums[start], nums[j] = nums[j], nums[start]
                start+=1
        return nums
                
                
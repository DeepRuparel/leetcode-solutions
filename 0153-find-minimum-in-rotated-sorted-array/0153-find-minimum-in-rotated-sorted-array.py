class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        while len(nums)!=1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            if left[-1] > right[-1]:
                nums = right
            else:
                nums = left
        return nums[0]
        
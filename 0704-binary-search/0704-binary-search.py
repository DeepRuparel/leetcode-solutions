class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1 and nums[0] == target:
            return 0
        while left <= right:
            mid = left + ((right - left) // 2) # prevents overflow 
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
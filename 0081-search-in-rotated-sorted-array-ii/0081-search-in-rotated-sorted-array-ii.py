class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1
        
        if left == right and nums[left] == target:
            return True
        
        while left <= right:
            if nums[left] == target:
                return True
            elif nums[right] == target:
                return True
            left += 1
            right -= 1
        
        return False
            
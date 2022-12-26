class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left+(right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid
            else:
                right = mid
            if left+1 == right:
                break
        
        if target <  nums[left] or target == nums[left]:
            mid = left
        elif target>nums[right]:
            mid = right + 1
        else:
            mid = right
        return mid
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findpivot(nums, left, right):
            if left > right:
                return -1
            if left == right:
                return left
            mid = left + (right- left)// 2
            
            if mid < right and nums[mid] > nums[mid + 1]:
                return mid + 1
            if mid > left and nums[mid] < nums[mid - 1]:
                return mid - 1
            if nums[left] > nums[mid]:
                return findpivot(nums, left, mid - 1)
            return findpivot(nums, mid +1, right)
        
        def bsearch(nums, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        pivot = findpivot(nums, 0, len(nums) - 1)
        
        if pivot == -1:
            return bsearch(nums, 0, len(nums) - 1, target)
        elif nums[pivot] == target:
            return pivot
        elif nums[0] <= target:
            return bsearch(nums, 0, pivot - 1, target)
        return bsearch(nums, pivot + 1, len(nums) -1 , target)
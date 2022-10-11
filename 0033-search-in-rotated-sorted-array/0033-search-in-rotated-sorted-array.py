class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findpivot(nums,left,right):
            if left > right:
                return -1
            if left == right:
                return left
            mid = (left+right)//2
            if mid < right and nums[mid]>nums[mid+1]:
                return mid+1
            elif mid > left and nums[mid] < nums[mid-1]:
                return mid-1
            elif nums[left] > nums[mid]:
                return findpivot(nums,left,mid-1)
            return findpivot(nums,mid+1,right)
        def binarysearch(nums,left,right,target):
            while left <= right:
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        
        pivot = findpivot(nums,0,len(nums)-1)
        if pivot == -1:
            return binarysearch(nums,0,len(nums)-1,target)
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return binarysearch(nums,0,pivot-1,target)
        return binarysearch(nums,pivot+1,len(nums)-1,target)
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums = sorted(nums)
        
        if len(nums)%2 != 0:
            return float(nums[(len(nums)//2)])
        else:
            if len(nums)%2 == 0:
                mid = len(nums)//2
                ans = nums[mid]+nums[mid-1]
                return float(ans/2)
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #using the kth largest element algorithm
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return (self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2 -1))/2
    
    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        index1 = len(nums1)//2
        index2 = len(nums2)//2
        m1 = nums1[index1]
        m2 = nums2[index2]
        
        # if k is greater then sums of indexs
        if index1 + index2 < k:
            # check if median of nums1 > median2
            #if yes then no need to include eleemnts till mb in nums2
            if m1 > m2:
                return self.kth(nums1, nums2[index2 +1:], k - index2 - 1)
            else:
                return self.kth(nums1[index1 + 1:], nums2, k - index1 -1)
        else:
            #if m1 > m2 it only includes elements till m1 in nums1
            if m1 > m2:
                return self.kth(nums1[:index1], nums2, k)
            else:
                return self.kth(nums1, nums2[:index2], k)
            
        
        
        
        
        
        #Brute force
#         nums = nums1+nums2
#         nums = sorted(nums)
        
#         if len(nums)%2 != 0:
#             return float(nums[(len(nums)//2)])
#         else:
#             if len(nums)%2 == 0:
#                 mid = len(nums)//2
#                 ans = nums[mid]+nums[mid-1]
#                 return float(ans/2)
        
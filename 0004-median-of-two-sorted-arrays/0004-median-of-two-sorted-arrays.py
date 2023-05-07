class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            
            ia = len(nums1)//2
            ib = len(nums2) // 2
            
            ma = nums1[ia]
            mb = nums2[ib]
            
            if ia + ib < k:
                if ma > mb:
                    return kth(nums1, nums2[ib+1 :], k -ib - 1)
                else:
                    return kth(nums1[ia + 1:], nums2, k - ia - 1)
            else:
                if ma > mb:
                    return kth(nums1[:ia], nums2, k)
                else:
                    return kth(nums1, nums2[:ib], k)
        l = len(nums1) + len(nums2)
        
        if l % 2 == 1:
            return kth(nums1, nums2, l//2)
        else:
            return ((kth(nums1, nums2, l//2) + kth(nums1, nums2, l//2 - 1)) / 2)
        
        
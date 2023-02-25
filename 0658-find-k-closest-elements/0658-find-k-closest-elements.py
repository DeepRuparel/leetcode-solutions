class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = left + (right - left)/ 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        ans = []
        
        for i in range(left, left + k):
            ans.append(arr[i])
        return ans
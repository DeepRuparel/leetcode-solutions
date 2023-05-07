class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = ans = 0
        
        while i < len(arr):
            base = i
            while i + 1 < len(arr) and arr[i] < arr[i+1]:
                i += 1
            
            # should be the peak so if peak == base means there is no uphill we increment i and conitinu
            if i == base:
                i += 1
                continue
            #this is the peak, now there should be a valley
            peak = i
            
            while i + 1 < len(arr) and arr[i] > arr[i+1]:
                i += 1
            # if there exists no valleryy we contine in search of next one
            
            if peak == i:
                i += 1
                continue
            ans = max(ans, i - base + 1)
        return ans
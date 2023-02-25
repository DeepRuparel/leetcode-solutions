class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isvalidsubstring(mid, k):
            freqmap = {}
            maxfreq = 0
            start = 0
            
            for end in range(len(s)):
                freqmap[s[end]] = freqmap.get(s[end], 0) + 1
                
                if end + 1 - start > mid:
                    freqmap[s[start]] -= 1
                    start += 1
                maxfreq = max(maxfreq, freqmap[s[end]])
                if mid - maxfreq <= k:
                    return True
            return False
        
        
        left = 0
        right = len(s) + 1
        
        while left + 1 < right:
            mid = left + (right -left) // 2
            
            if isvalidsubstring(mid, k):
                left = mid
            else:
                right = mid
        return left
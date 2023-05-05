class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        fans = 0
        ans = 0
        left = 0
        right = 0
        
        while right < len(s):
            if right - left < k:
                if s[right] in {'a', 'e', "i", 'o', 'u'}:
                    ans += 1
                    fans = max(ans, fans)
                right += 1
            else:
                #fans = max(ans, fans)
                while right - left >= k:
                    if s[left] in {'a', 'e', "i", 'o', 'u'}:
                        ans -= 1
                    left += 1
                #right += 1

        #return ans
                
        return fans
        
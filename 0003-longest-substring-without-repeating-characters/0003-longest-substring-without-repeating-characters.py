'''
Idea is once see a repating chacter we start popping from the left until that chatacter isn't present in seen
maintain a global res and res = max(res, new length that we found)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        return res
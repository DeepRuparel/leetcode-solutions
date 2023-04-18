class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = min(len(word1), len(word2))
        ans = ''
        for i in range(l):
            ans += word1[i]
            ans += word2[i]
        
        if len(word1) > l:
            for i in range(l, len(word1), 1):
                ans += word1[i]
        if len(word2) > l:
            for i in range(l, len(word2), 1):
                ans += word2[i]
        return ans
        
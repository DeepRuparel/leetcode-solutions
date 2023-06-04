class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s1 = list(s)
        while l < r:
            while l < r and s1[l] not in 'aeiouAEEIOU':
                l += 1
            while l < r and s1[r] not in 'aeiouAEIOU':
                r -= 1
            
            if l < r:
                s1[l], s1[r] = s1[r], s1[l]
            l += 1
            r -= 1
        return "".join(s1)
        
        
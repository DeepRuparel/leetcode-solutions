class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left,right):
            while left < right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
            
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left]!=s[right]:
                palleft = isPalindrome(left+1,right)
                palright = isPalindrome(left,right-1)
                
                return palleft or palright
            left+=1
            right-=1
        return True
        
        
        
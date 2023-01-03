class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(curr, start):
            if start == len(s):
                ans.append(curr[:])
            else:
                for i in range(start, len(nums)):
                    if isPalindrome(start, i):
                        curr.append(s[start:i+1])
                        backtrack(curr,i+1)
                        curr.pop()
        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        nums = list(s)
        ans = []
        backtrack([],0)
        return ans
                    
        
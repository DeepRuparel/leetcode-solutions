class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = 0
        j = 0
        n = len(start)
        while i < n or j < n:
            
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X' :
                j += 1
                
            if i != j and (i==n or j == n):
                return False
            if i == j and i == n:
                return True
            
            if start[i] != end[j]:
                return False
            
            if start[i] == 'L' and j > i:
                
                return False
            if start[i] == 'R' and j < i:
                
                return False
            
            i+=1 
            j+=1
        return True
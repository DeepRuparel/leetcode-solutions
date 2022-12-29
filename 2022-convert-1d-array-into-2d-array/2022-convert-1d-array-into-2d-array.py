class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        row , col = 1, len(original)
        if row*col != m*n:
            return []
        ans = []
        for i in range(m):
            temp = []
            for i in range(n):
                temp.append(original.pop(0))
            ans.append(temp)
        return ans
            
                
            
            
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while left < right and top < bottom:
            if matrix[top][right-1] == target:
                return True
            if matrix[top][right-1] > target:
                right-=1
            else:
                top+=1
        return False
        
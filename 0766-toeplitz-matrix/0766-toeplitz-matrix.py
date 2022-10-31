class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal = {}
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i - j not in diagonal:
                    diagonal[i-j] = matrix[i][j]
                elif diagonal[i-j] != matrix[i][j]:
                    return False
        return True
                
                
                
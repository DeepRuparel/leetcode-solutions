class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        visit = set()
        ans = 0
        for i in range(len(mat)):
            visit.add((i, i))
            ans += mat[i][i]
        
        i = 0
        j = len(mat) - 1
        
        while i != len(mat):
            if (i,j) not in visit:
                ans += mat[i][j]
            i+=1
            j-=1
        return ans
            
        
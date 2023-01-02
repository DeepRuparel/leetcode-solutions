class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        def is_valid(i,j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False
        def get_neighbors(i,j):
            return [(i+1,j),(i-1,j), (i,j+1), (i,j-1)]
        
        def dfs(i,j,index):
            if index == len(word):
                return True
            
            for nei in get_neighbors(i,j):
                x,y = nei
                if is_valid(x,y) and (x,y) not in visited and board[x][y] == word[index]:
                    visited.add((x,y))
                    if dfs(x,y,index+1):
                        return True
                    visited.remove((x,y))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if dfs(i,j,1):
                        return True
        return False
    
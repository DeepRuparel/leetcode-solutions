class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # we will do a bfs
        queue = deque([1])
        steps = 0
        n = len(board)
        visisted= []
        def getcoords(num):
            # row from top
            rt = (num-1)//n
            # row from bottom
            rb = (n-1) - rt
            
            col = (num-1)%n
            if (n%2 == 1 and rb%2 == 1) or (n%2 == 0 and rb % 2 == 0 ):
                col = (n-1) - col
            return [rb, col]
        
        for i in range(n):
            visisted.append([False]*n)
        # marking the first square as visisted
        visisted[n-1][0] = True
        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                #print(x)
                if x == n*n:
                    return steps
                
                
                # all the things i can go from z ir x+1, x+2
                for i in range(1, 7):
                    val = x + i
                    if val > n*n:
                        break
                    
                    coords = getcoords(val)
                    r = coords[0]
                    c = coords[1]
                    
                    if (visisted[r][c]):
                        continue
                    visisted[r][c] = True
                    if board[r][c] == -1:
                        queue.append(val)
                    else:
                        queue.append(board[r][c])
            steps += 1
        return -1
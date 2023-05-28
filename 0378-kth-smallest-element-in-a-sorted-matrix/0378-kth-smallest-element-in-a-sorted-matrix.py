class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for i in range(len(matrix)):
            heapq.heappush(h, [matrix[i][0], i, 0])
        
        while k!=1:
            element, curr_matrix, index = heapq.heappop(h)
            if index + 1 < len(matrix[curr_matrix]):
                heapq.heappush(h, [matrix[curr_matrix][index + 1], curr_matrix, index + 1])
            k -= 1
        
        if h:
            element, curr_matrix, index = heapq.heappop(h)
            return element
        return -1
            
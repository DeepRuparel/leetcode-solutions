class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        for i in grid:
            l = 0
            r = n- 1
            while l <= r:
                mid = (l + r) // 2
                if i[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1
            ans += n - l
        return ans
                    
                
        
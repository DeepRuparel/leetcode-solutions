class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        right = sum(weights) 
        left = max(weights)
        
        while left < right:
            mid = (left+right)//2
            cur = 0
            need = 1
            for weight in weights:
                if cur+weight > mid:
                    need+=1
                    cur = 0
                cur += weight 
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left
                
        
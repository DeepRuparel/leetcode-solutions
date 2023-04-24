class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones, reverse = True)
        
        
        
        i = 0
        while i < len(stones):
            stones = sorted(stones, reverse = True)
            if len(stones) >= 2:
                x = stones.pop(0)
                y = stones.pop(0)
                
                if x != y:
                    stones.append(abs(x-y))
            else:
                break
        

        if stones:
            return stones[0]
        else:
            return 0
            
            
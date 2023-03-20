class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        for i in range(1, len(flowerbed) - 1):
            if n:
                if i == 1 and (flowerbed[0] == 0 and flowerbed[i] == 0):
                    flowerbed[0] = 1
                    n-=1
                    continue
                if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1 and flowerbed[i] == 0:
                    #print(i)
                    flowerbed[i] = 1
                    n -= 1
        
        if n and (flowerbed[-1] == 0 and flowerbed[-2] == 0):
            flowerbed[-1] = 1
            n -= 1
        if n == 0:
            return True
        return False
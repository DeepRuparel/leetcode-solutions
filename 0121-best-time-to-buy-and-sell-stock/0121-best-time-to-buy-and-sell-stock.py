'''
intuition find the minimum and then find the maximum thqat comes after iit 
so 
left = 0
right = 0 to len(prices)

[7, 1, 5, 3, 6, 4]
    l
                   r
    
r - l = 7 -7 = 0 <- curr profit
maxprofit = max(currprofut, currprofit)  = 0
r - l = 1 - 7 = -6 mp = 0
since it is less than zero i will make left - right because it is the minimum so far
r - l = 5 - 1 = 4 mp = 4
r - l = 3 - 1 - 2 mp = 4
r - l = 6 - 1 = 5 mp = 5
r - l = 4 - 1 = 3 mp = 5
return mp

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit  = 0
        left = 0
        
        
        for right in range(len(prices)):
            currprofit = prices[right]-prices[left]
            maxprofit = max(currprofit, maxprofit)
            if currprofit<0:
                left = right
        return maxprofit
                
            
        
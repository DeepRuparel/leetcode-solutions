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
                
            
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minimum = 0
        maximum = 0
        price = 0
        while price < len(prices)-1:
            while price<len(prices)-1 and prices[price] >= prices[price+1]:
                price+=1
            minimum = prices[price]
            while price<len(prices)-1 and prices[price] <= prices[price+1]:
                price+=1
            maximum = prices[price]
            answer += maximum-minimum
        return answer
            
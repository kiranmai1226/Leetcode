class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in prices:
            min_price = min(i,min_price)
            profit = max(profit,i-min_price)
        return profit
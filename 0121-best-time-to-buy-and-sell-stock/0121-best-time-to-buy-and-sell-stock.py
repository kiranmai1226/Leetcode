class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_val = float(inf)
        for i in range(1,len(prices)):
            min_val = min(prices[i-1],min_val)
            max_price = max(max_price, prices[i]-min_val)
        return max_price
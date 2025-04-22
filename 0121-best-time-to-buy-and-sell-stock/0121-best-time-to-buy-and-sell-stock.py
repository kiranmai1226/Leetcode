class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            minimum=min(prices[i],minimum)
            profit=prices[i]-minimum
            max_profit=max(profit,max_profit)
        return max_profit
        

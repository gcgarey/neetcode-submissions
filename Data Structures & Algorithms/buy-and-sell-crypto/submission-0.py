class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                new_profit = prices[j] - prices[i]
                if new_profit > max_profit:
                    max_profit = new_profit
        return max_profit
        
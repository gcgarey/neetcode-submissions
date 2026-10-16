class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = 0
        s = 1
        while s < len(prices):
            temp_profit = prices[s] - prices[b]
            profit = max(profit, temp_profit)

            if prices[s] <= prices[b]:
                b = s
            s += 1
        return profit



        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = 0
        s = 1
        while s < len(prices):
            if prices[b] < prices[s]:
                profit = max(profit, prices[s] - prices[b])
            else:
                b = s
            s += 1
        return profit



        
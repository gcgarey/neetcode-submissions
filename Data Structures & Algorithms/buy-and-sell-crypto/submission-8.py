class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = 0
        for s in range(1, len(prices)):
            t = prices[s] - prices[b]
            p = max(t, p)
            if prices[s] < prices[b]:
                b = s
        return p

        
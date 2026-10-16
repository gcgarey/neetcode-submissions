class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
                
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            if amount == 0:
                return 0

            res = 1000000000000
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            dp[amount] = res
            return res

        minCoins = dfs(amount)
        if minCoins >= 1000000000000:
            return -1
        else:
            return minCoins
        


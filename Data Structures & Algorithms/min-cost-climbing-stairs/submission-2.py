class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0] * len(cost)
        mincost[-1] = cost[-1]
        mincost[-2] = cost[-2]

        for i in range(len(mincost)-3, -1, -1):
            mincost[i] = cost[i] + min(mincost[i + 1], mincost[i + 2])
        return min(mincost[0], mincost[1])
        

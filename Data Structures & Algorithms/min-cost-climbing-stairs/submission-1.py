class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [0] * len(cost)
        steps.append(0)
        steps[-2] = cost[-1]
        
        for i in range(len(steps)-3, -1, -1):
            print(i)
            steps[i] = min(cost[i] + steps[i+1], cost[i] + steps[i+2])
        print(steps)

        return min(steps[0], steps[1])
        

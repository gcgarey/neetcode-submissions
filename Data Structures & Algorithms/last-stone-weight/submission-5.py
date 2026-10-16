class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            print(f"x is {x} y is {y}")
            if y <= x:
                heapq.heappush(stones, (y - x))
    
        return -(stones[0])
            


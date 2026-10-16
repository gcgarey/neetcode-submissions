class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to max heap
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 2:
            # pop the two heaviest stones 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, -(y-x))

        if len(stones) < 2:
            return -stones[0]
        
        x, y = stones[0], stones[1]
        if x == y:
            return 0
        return y - x


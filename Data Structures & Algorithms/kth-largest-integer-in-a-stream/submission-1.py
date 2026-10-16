class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []

        for num in nums: 
            self.add(num)
        
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else: 
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]
        
        

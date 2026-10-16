class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        minHeap = heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # add the value to the heap
        heapq.heappush(self.minHeap, val)
        
        # if the heap is bigger than k, pop the smallest value
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # return the kth largest (root)
        return self.minHeap[0]
        
        

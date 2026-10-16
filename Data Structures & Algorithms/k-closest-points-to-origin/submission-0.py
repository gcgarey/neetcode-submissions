class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            dist = -(math.sqrt((points[i][0])**2 + (points[i][1])**2))
            minHeap.append((dist, points[i][0], points[i][1]))

        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)

        res = []
        for i in range(len(minHeap)):
            res.append([minHeap[i][1], minHeap[i][2]])

        return res

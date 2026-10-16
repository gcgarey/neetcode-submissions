class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a dictionary to count the frequency of tasks
        freq = Counter(tasks)
        # create a max heap to organize the most frequent tasks
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        # constant to keep track of time
        time = 0
        # queue to keep track of how much idle time we have [task, idleTime]
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                task = q.popleft()
                heapq.heappush(maxHeap, task[0])
        return time


        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            
            if len(res) < k:
                res.append(nums[i])
                if len(res) == k:
                    heapq.heapify(res)
            else:
                if nums[i] > res[0]:
                    heapq.heappop(res)
                    heapq.heappush(res, nums[i])
        return res[0]

        
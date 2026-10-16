class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sort_freq = [[] for i in range(len(nums) + 1)] 
        res = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        print(freq)
        
        for val in freq:
            sort_freq[freq[val]].append(val)

        # print(sort_freq)

        for i in range(len(sort_freq)-1, -1, -1):
            for j in sort_freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        
        
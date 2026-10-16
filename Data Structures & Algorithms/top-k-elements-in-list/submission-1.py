class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # define our dictionary and list of length(nums)
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        #populate the count dictionary with the number of times each num appears
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        #for each frequency, put that key into freq
        for key, val in count.items():
            freq[val].append(key)

        #traverse freq backwards and return the first k elements
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        

        
        
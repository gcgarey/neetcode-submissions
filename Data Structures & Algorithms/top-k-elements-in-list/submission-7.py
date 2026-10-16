class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find frequency of each element
        freq = defaultdict(int) # num: freq
        res = []
        temp = [[] for _ in range(len(nums)+1)]

        # find frequency of each number
        for num in nums:
            freq[num] += 1
        # put numbers into temp based on frequency
        for num, f in freq.items():
            temp[f].append(num)

        # put the k most frequent elements in res
        for i in range(len(temp)-1, -1, -1):
            for n in temp[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
        
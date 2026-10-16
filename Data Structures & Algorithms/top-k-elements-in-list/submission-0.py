class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

       # create a hashmap to keep track of how many times a number shows up
       counts = {}

       # populate that hashmap
       for num in nums:
        counts[num] = counts.get(num, 0) + 1

       # crate a list of lists, where each sublist is how many values show up at the index's time
       frequency = [[] for i in range(len(nums) + 1)]
       #populate that list of lists
       for key, val in counts.items():
        frequency[val].append(key)

       #create a list to store the result
       result = []

       # traverse frequency backwards to find the k most common numbers
       for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result

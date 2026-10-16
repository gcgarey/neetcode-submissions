class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find frequency of each element
        n = len(nums) + 1
        temp = [[] for _ in range(n)]
        freq = defaultdict(int)
        res = []

        for num in nums:
            freq[num] += 1

        for num in freq:
            temp[freq[num]].append(num)

        for i in range(len(temp)-1, -1, -1):
            for j in range(len(temp[i])):
                res.append(temp[i][j])
                if len(res) == k:
                    return res
        
            
        
        print(temp)
        
        

        '''for i in range(len(temp)-1, -1, -1):
            if temp[i] != 0:
                res.append(temp[i])
            if len(res) == k:
                return res'''

        return []
        
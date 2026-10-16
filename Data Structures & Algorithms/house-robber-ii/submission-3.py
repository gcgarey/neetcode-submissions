class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        n = len(nums)
        first = [0] * n 
        last = [0] * n 

        first[0], first[1] = nums[0], nums[1]
        for i in range(2, n-1):
            first[i] = max((nums[i] + max(first[i-2], first[i-3])), first[i-1])
        print(first)
        
        last[1], last[2] = nums[1], nums[2]
        for j in range(3, n):
            last[j] = max((nums[j] + max(last[j-2], last[j-3])), last[i-1])
        print(last)
        
        return max(last[-1], last[-2], first[-1], first[-2])
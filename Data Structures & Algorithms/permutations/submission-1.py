class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(left, curr):
            if len(curr) == len(nums):
                res.append(curr)
                return

            for i in range(len(left)):
                dfs(left[:i] + left[i+1:], curr + [left[i]])
                
        
        dfs(nums, [])

        return res
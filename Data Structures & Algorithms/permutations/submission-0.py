class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(left, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(left)):
                curr.append(left[i])
                dfs(left[:i] + left[i+1:], curr)
                curr.pop()
        
        dfs(nums, [])

        return res
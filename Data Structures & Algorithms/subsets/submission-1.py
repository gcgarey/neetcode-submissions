class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(temp, i):
            if i >= len(nums) and temp not in res:
                res.append(temp[:])
                return

            # choose element
            temp.append(nums[i])
            dfs(temp, i + 1)

            # dont choose element
            temp.pop()
            dfs(temp, i + 1)
        
        dfs([], 0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtrack(idx):
            if idx == n:
                res.append(sol[:])
                return None
            
            backtrack(idx+1)

            sol.append(nums[idx])
            backtrack(idx+1)
            sol.pop()

        backtrack(0)
        return res
        
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(total, i):
            if total == target:
                res.append(sol.copy())
                return
            if total > target or i >= n:
                return

            # not include element
            backtrack(total, i+1)

            # include element
            sol.append(nums[i])
            backtrack(total + nums[i], i)
            sol.pop()

        backtrack(0, 0)
        return res
        
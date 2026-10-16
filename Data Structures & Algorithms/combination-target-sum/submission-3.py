class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)-1

        def backtrack(idx, total):
            if total == target:
                res.append(sol.copy())
                return
            if idx > n or total > target:
                return None
            
            # move on
            backtrack(idx+1, total)
                
            # include number
            sol.append(nums[idx])
            backtrack(idx, total + nums[idx])
            sol.pop()

        backtrack(0, 0)
        return res
                
        
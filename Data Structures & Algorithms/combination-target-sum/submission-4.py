class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        n = len(nums)-1

        def backtrack(total, i):
            if total == target:
                res.append(sol.copy())
                return
            if i > n or total > target:
                return

            backtrack(total, i+1)

            sol.append(nums[i])
            backtrack(total+nums[i], i)
            sol.pop()

        backtrack(0, 0)
        return res

            

        
                
        
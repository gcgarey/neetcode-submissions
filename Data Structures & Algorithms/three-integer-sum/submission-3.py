class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] > -a:
                    r -= 1
                elif nums[l] + nums[r] < -a:
                    l += 1
                else:
                    res.append((nums[l], a, nums[r]))
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

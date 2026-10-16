class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
            
        money = [0] * len(nums)
        money[-1], money[-2] = nums[-1], max(nums[-1], nums[-2])

        for i in range(len(nums)-3, -1, -1):
            money[i] = max(money[i+1], nums[i] + money[i+2])
        return money[0]
         
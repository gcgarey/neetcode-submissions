class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        money = [-1] * len(nums)
        money[-1] = nums[-1]
        money[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1, -1):
            money[i] = max(money[i+1], nums[i] + money[i+2])

        print(money)
        return max(money[0], money[1])   
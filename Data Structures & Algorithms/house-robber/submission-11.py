class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        money = [0] * n
        if n < 2:
            return nums[0]
        money[0], money[1] = nums[0], nums[1]
        for i in range(2, n):
            if i < 3:
                money[i] = nums[i] + money[i-2]
            else:
                money[i] = nums[i] + max(money[i-2], money[i-3])
        return max(money[-1], money[-2])

        
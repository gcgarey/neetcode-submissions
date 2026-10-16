class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        money1 = [-1] * len(nums[:-1])
        money2 = [-1] * len(nums[1:])
        
        money1[-1], money1[-2] = nums[-2], max(nums[-2], nums[-3])
        money2[-1], money2[-2] = nums[-1], max(nums[-2], nums[-1])
        
        for i in range(len(money1)-3, -1, -1):
            money1[i] = max(money1[i+1], nums[i] + money1[i+2])

        for i in range(len(money2)-3, -1, -1):
            money2[i] = max(money2[i+1], nums[i+1] + money2[i+2])

        return max(money1[0], money2[0])
            

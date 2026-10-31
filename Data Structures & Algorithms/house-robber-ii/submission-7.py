class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        money1 = [0] * (n-1) # first - second to last
        money2 = [0] * (n-1) # second - last
        
        money1[0], money1[1] = nums[0], nums[1]
        money2[0], money2[1] = nums[1], nums[2]

        for i in range(2, n-1):
            if i < 3:
                money1[i] = nums[i] + money1[i-2]
                money2[i] = nums[i+1] + money2[i-2]
            else:
                money1[i] = nums[i] + max(money1[i-2], money1[i-3])
                money2[i] = nums[i+1] + max(money2[i-2], money2[i-3])
        
        return max(money1[-1], money1[-2], money2[-1], money2[-2])
            

        
        
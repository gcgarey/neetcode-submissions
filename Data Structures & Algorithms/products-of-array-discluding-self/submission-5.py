class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        temp1 = 1
        for i in range(len(nums)-1):
            res[i] = temp1
            temp1 *= nums[i]
        res[-1] = temp1
        temp2 = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= temp2
            temp2 *= nums[i]
        return res
        
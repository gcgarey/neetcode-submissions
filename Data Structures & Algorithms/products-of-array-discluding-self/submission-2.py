class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a res array and a prefix variable
        res = [1] * len(nums)
        prefix = 1

        # iterate through nums:
        for i in range(len(nums)):
            # update res array with prefix 
            res[i] *= prefix
            # update prefix with prefix * nums[i]
            prefix *= nums[i]

        postfix = 1

        # iterate through nums backwards
        for i in range(len(nums)-1, -1, -1):
            # update res with *= postfix
            res[i] *= postfix
            # update postfix with *= nums[i]
            postfix *= nums[i]

        return res
        
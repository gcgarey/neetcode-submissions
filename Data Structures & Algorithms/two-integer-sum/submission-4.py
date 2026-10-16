class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {} # number : idx
        for i in range(len(nums)):
    
            x = target - nums[i]
            if x in num_set:
                return [num_set[x], i]

            num_set[nums[i]] = i


        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        contains = {} # arr[i] --> index
        for i in range(len(nums)):
            if target - nums[i] in contains:
                return [contains[target - nums[i]], i]
            contains[nums[i]] = i

        
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in have:
                return [have[need], i]
            else:
                have[nums[i]] = i
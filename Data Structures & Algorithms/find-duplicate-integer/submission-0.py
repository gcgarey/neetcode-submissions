class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == -1:
                return i
            jump = nums[i]
            nums[i] = -1
            i = jump

        


        
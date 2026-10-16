class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDupes = False
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    hasDupes = True
                    return hasDupes
        return hasDupes
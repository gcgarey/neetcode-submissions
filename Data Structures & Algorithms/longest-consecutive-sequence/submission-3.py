class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            temp_length = 1
            while num + 1 in nums:
                temp_length += 1
                num += 1
            max_length = max(max_length, temp_length)

        return max_length 
        
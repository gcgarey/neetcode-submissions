class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            # find start of sequence
            if num - 1 not in nums:
                temp_length = 0
                temp_val = num
                while temp_val in nums:
                    temp_length += 1
                    temp_val += 1
                max_length = max(max_length, temp_length)
        return max_length

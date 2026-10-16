class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn nums into set for fast lookups
        nums = set(nums)

        max_length = 0
        # iterate through set
        for num in nums:
            # if num[i] - 1 is not in the set: we found the beginning
            if num - 1 not in nums:
                # keep a variable to track max count
                temp_length = 0
                temp_val = num
                while temp_val in nums:
                    temp_length += 1
                    temp_val += 1
                max_length = max(max_length, temp_length)

        # return max length
        return max_length
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 0
        for num in nums:
            if num - 1 not in nums:
                temp_length = 0
                temp_num = num
                while temp_num in nums:
                    temp_length += 1
                    temp_num += 1
                if temp_length > length:
                    length = temp_length
        return length


        
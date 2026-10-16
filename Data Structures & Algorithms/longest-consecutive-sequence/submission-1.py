class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set()
        for num in nums:
            sequence.add(num)
        
        max_s = 0
        for i in range(len(nums)):
            temp_s = 1
            while nums[i] + 1 in sequence:
                temp_s += 1
                nums[i] += 1
            max_s = max(max_s, temp_s)
        return max_s

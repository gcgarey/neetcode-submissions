class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        for i in range(len(nums)-3, -1, -1):
            biggest = nums[i+2]
            print(f"{biggest} and {i}")
            for j in range(i+2, len(nums)):
                biggest = max(biggest, nums[j])
            nums[i] += biggest

        print(nums)
        
        
        return max(nums[0], nums[1])
        
            

        
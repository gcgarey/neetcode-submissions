class Solution:
    def jump(self, nums: List[int]) -> int:
        r = 0
        l = 0
        index = 0
        while r < len(nums)-1:
            maxIndex = 0
            for j in range(l, r+1):
                maxIndex = max(j + nums[j], maxIndex)
            l = r + 1
            r = maxIndex
            index += 1
        return index 

            
        
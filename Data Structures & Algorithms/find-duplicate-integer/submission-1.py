class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            val = nums[i]
            if val == 0:
                return i
            nums[i] = 0
            i = val


        

        


        
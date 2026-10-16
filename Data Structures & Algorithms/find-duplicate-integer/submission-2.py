class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if nums[s] == nums[f]:
                i = 0
                while nums[s] != nums[i]:
                    s = nums[s]
                    i = nums[i]
                return nums[s]
                
            
        return 0
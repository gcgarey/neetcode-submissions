class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i in nums:
            if i not in dups:
                dups[i] = 0
            else: 
                return True
        return False
        

        
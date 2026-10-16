class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for i in nums:
            if i in dupes:
                return True
            else:
                dupes[i] = 0
        
        return False

        
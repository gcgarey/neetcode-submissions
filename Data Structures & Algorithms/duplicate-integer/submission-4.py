class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for i in nums:
            if i not in dupes:
                dupes[i] = 1
            else:
                return True
        return False
        

        
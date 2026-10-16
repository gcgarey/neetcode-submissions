class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            res = (l + r) // 2
            if nums[res] == target:
                return res
            elif nums[res] > target:
                r = res - 1
            else:
                l = res + 1
        return -1
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #define my left and right pointers
        l = 0
        r = len(nums) - 1
        # make a variable to hold the min
        res = nums[0]

        # while left < right
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            print("l")

            mid = (l + r) // 2
            res = min(nums[mid], res)

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res
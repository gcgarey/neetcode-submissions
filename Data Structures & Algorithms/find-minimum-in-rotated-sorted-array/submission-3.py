class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            mid = (l + r) // 2
            # if the list is ascending, right pointer 
            if nums[l] <= nums[mid]:
                l = mid + 1
                res = min(res, nums[mid])
            else:
                r = mid - 1
                res = min(res, nums[mid])
                

        return res
        
        
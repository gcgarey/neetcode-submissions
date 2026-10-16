class Solution:
    def findMin(self, nums: List[int]) -> int:
        # define what I need
        l = 0
        r = len(nums) - 1
        res = nums[-1]
        # start the binary search
        while l <= r:
            # account for the edge case
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break 

            mid = (r + l) // 2
            res = min(res, nums[mid])
            # compare the middle to the left
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        #return result
        return res
        
        
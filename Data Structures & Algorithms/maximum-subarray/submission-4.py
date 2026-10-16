class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max_total = nums[0]
        # loop through each element of array
        for i in range(1, len(nums)):
        # eplore option 1: add to sum
            temp_total = total + nums[i]
            print(f"temp total is {temp_total} nums[i] is {nums[i]} ")
        # explore option 2 start fresh

        # choose the larger option
            if temp_total > nums[i]:
                total = temp_total
            else:
                total = nums[i]
            
            if total > max_total:
                max_total = total
            print(f"total is {total}")

        # return the sum at the end
        return max_total
        


        
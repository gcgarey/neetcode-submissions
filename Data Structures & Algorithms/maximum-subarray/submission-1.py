class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        # add the current element to currSum
        def addNew(val, s):
            return s + val

        # start a new subarray
        def startNew(val):
            return val

        # iterate through list and track maximum sum at each step
        for i in range(len(nums)):
            x = addNew(nums[i], currSum)
            y = startNew(nums[i])
            if x > y:
                currSum = x
                print(f"x is {x} currsum is {currSum}")
            else:
                currSum = y
                print(f"y is {y} currsum is {currSum}")

            if currSum > maxSum: 
                maxSum = currSum

        return maxSum


        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create the result list and sort initial array
        nums.sort()
        res = []

        # iterate through the index and values
        for i, a in enumerate(nums):
            # if we are not at the first index and the first element is the same, skip
            if i > 0 and a == nums[i-1]:
                continue

            #create your left and right pointers and do twosum
            l, r = i + 1, len(nums) -1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                    # if they pass through add to result
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res




        
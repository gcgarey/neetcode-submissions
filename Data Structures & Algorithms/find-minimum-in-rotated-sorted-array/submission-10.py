class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minn = nums[0]
        while l <= r:
            mid = (l + r) // 2
            minn = min(minn, nums[mid])
            print(f"{nums[l]}, {nums[r]}, {minn}, {nums[mid]}")
            if nums[r] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            print(f"test : {l}, {r}")
        return minn
                


        
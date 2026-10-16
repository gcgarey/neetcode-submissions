class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left side is sorted
            if nums[l] <= nums[mid]:
                # target is in sorted range
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                # target not in sorted range
                else:
                    l = mid + 1

            #right side is sorted
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res

        

        
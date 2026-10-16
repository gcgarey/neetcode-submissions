class Solution:
    def trap(self, height: List[int]) -> int:
        # water at index i can be calculated with min(height[l], height[r] - height[i])
        maxL = height[0]
        maxR = height[-1]
        l, r = 0, len(height) - 1
        water = 0
        while l < r:
            if maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                if maxR - height[r] > 0:
                    water += (maxR - height[r])
            else:
                l += 1
                maxL = max(maxL, height[l])
                if maxL - height[l] > 0:
                    water += maxL - height[l]
        return water



        
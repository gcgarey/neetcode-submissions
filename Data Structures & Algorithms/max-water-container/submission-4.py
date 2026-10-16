class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water = min(height[i], height[j]) * i - j
        max_water = 0 
        l, r = 0, len(heights) - 1
        while l <= r:
            print(f"l: {heights[l]}, r: {heights[r]}")
            temp_water = min(heights[l], heights[r]) * (r - l)
            max_water = max(max_water, temp_water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
        
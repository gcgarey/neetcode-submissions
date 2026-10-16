class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most_water = 0
        l = 0
        r = len(heights)-1
        while l < r:
            water = (r-l) * min(heights[l], heights[r])
            most_water = max(most_water, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most_water
class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)
        left_height = 0
        right_height = 0
        for i in range(len(height)-1):
            for j in range(0, i):
                if height[j] > left_height:
                    left_height = height[j]
            for l in range(i+1, len(height)):
                if height[l] > right_height:
                    right_height = height[l]
            area = min(left_height, right_height) - height[i]
            if area > 0:
                water[i] = area
            right_height, left_height = 0, 0
        return sum(water)
        
            

        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # [[idx, height]]
        maxA = 0
        for i in range(len(heights)):
            start = i
            while s and heights[i] < s[-1][1]:
                idx, h = s.pop()
                start = idx
                maxA = max(maxA, (i - idx) * h)

            s.append([start, heights[i]])
        while s:
            i, h = s.pop()
            maxA = max(maxA, h * (len(heights)-i))
        return maxA

            
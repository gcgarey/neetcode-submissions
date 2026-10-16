class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackval, stackinx = stack.pop()
                output[stackinx] = i - stackinx
                

            stack.append((temp, i))

        return output
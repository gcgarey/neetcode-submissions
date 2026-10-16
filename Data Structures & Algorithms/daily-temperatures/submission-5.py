class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[temp, idx]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                warm = stack.pop()
                res[warm[1]] = i - warm[1]
            stack.append([temperatures[i], i])

        return res 


        
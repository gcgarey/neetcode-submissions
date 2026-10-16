class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [ (val, idx), ...]
        for i in range(len(temperatures)):
            temp_idx = i
            while stack and stack[-1][0] < temperatures[i]:
                val, idx = stack.pop()
                res[idx] = temp_idx - idx
            
            stack.append((temperatures[i], i))

        return res




        
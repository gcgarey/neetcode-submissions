class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        stack = []
        for p in range(len(position)):
            combined.append((position[p], speed[p]))
        combined.sort()
        
        for i in range(len(combined)):
            print(stack)
            time = (target - combined[i][0]) / combined[i][1]
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)

        return len(stack)

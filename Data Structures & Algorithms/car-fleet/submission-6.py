class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        stack = []

        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        combined.sort(reverse=True)
        
        for i in range(len(combined)):
            time = (target - combined[i][0]) / combined[i][1]
            print(time)
            if not stack:
                stack.append(time)
            if stack and time > stack[-1]:
                stack.append(time)

        print(stack)

        return len(stack)
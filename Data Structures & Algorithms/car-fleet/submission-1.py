class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for car in range(len(position)):
            cars.append((position[car], speed[car]))
        cars.sort(reverse=True)
        
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][-1]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        print(stack)
        return len(stack)


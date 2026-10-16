class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        for car in cars:
            arrive = (target - car[0]) / car[1]
            if stack and arrive <= stack[-1]:
                continue
            else:
                stack.append(arrive)

        return len(stack)
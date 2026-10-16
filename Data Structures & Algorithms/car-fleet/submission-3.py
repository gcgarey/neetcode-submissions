class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        

        for i in range(len(cars)):
            length = (target - cars[i][0]) / cars[i][1]
            print(f"length: {length}")
            print(f"car position: {cars[i][0]} cars speed: {cars[i][1]}")
            
            if stack and length <= stack[-1]:
                continue
            else:
                stack.append(length)
        print(stack)

        return len(stack)
            
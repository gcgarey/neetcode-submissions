class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pt = {} # {position : time}
        for i in range(len(position)):
            pt[position[i]] = speed[i]


        for p, s in sorted(pt.items()):
            end = (target - p) / s
            while stack and end >= stack[-1]:
                stack.pop()
            stack.append(end) 
        
        return len(stack)


        
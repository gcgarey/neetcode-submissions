class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if t == '+':
                    temp = val1 + val2
                
                elif t == '-':
                    temp = val2 - val1
            
                elif t == '*':
                    temp = val1 * val2
                
                else:
                    temp = val2 / val1
                
                stack.append(int(temp))
            
            else:
                stack.append(int(t))

        
        return stack[-1]

        
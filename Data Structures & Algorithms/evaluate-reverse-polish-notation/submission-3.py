class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if tokens[i] == '+':
                    total = operand1 + operand2
                elif tokens[i] == '-':
                    total = operand2 - operand1
                elif tokens[i] == '*':
                    total = operand1 * operand2
                else:
                    total = operand2 / operand1
                stack.append(int(total))
                print(f"operand1: {operand1}, operand2: {operand2} total: {total}")
            else:
                stack.append(int(tokens[i]))
        return stack[0]

        
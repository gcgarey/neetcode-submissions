class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char in mapping:
                if not stack or mapping[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False

        
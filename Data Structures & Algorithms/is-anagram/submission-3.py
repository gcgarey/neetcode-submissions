class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}

        for char in s:
            if char not in s_char:
                s_char[char] = 1
            else:
                s_char[char] += 1

        for char in t:
            if char not in t_char:
                t_char[char] = 1
            else:
                t_char[char] += 1

        if s_char == t_char:
            return True
        else:
            return False
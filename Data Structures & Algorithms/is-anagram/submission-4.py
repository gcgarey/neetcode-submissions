class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}
        for let in s:
            s_char[let] = s_char.get(let, 0) + 1
        
        for let in t:
            t_char[let] = t_char.get(let, 0) + 1
        
        return s_char == t_char
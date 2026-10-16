class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_order = {}
        t_order = {}

        for char in s:
            if char not in s_order:
                s_order[char] = 1
            else:
                s_order[char] += 1
        
        for char in t:
            if char not in t_order:
                t_order[char] = 1
            else:
                t_order[char] += 1

        return s_order == t_order
        
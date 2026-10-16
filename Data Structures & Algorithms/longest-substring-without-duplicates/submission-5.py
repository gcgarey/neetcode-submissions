class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        substring = set()
        l, r = 0, 0

        while r < len(s):
            # if s[r] that is in substring, empty it and move l
            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[r])
            res = max(len(substring), res)
            r += 1

        return res
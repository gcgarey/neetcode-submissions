class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 0
        chars = {}

        while r < len(s):
            chars[s[r]] = 1 + chars.get(s[r], 0)

            while chars[s[r]] > 1:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1

            longest = max(longest, len(chars))
            r += 1
        return longest
        
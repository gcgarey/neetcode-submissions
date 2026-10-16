class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        seen = {}
        res = 0
        # if we havent seen the element, include it in the window
        while end < len(s):
            if s[end] not in seen:
                seen[s[end]] = 1
        # if we have a duplicate, move start of window until we don't
            else:
                seen[s[end]] += 1
                while seen[s[end]] > 1:
                    seen[s[start]] -= 1
                    if seen[s[start]] == 0:
                        del seen[s[start]]
                    start += 1
            res = max(res, len(seen))
            end += 1
        return res

        
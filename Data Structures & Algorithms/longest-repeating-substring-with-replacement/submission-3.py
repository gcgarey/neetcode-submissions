class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            windowlen = r - l + 1
            while windowlen - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                windowlen = r - l + 1
            res = max(res, windowlen)

        return res 
                

        
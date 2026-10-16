class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # string valid if len(window) - most freq char <= k
        longest = 0
        r, l = 0, 0
        freq = {}

        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
            r += 1

        return longest
    
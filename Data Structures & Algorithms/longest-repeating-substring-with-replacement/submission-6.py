class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length(r - l) - count most frequenty element <= k
        longest = 0
        freq = defaultdict(int)
        l, r = 0, 0

        while r < len(s):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest


        
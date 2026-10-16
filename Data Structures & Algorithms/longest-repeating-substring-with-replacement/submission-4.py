class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        freq = defaultdict(int)
        while r < len(s):
            print(f"{s[l]}, {s[r]}")
            freq[s[r]] += 1
            while ((r - l) - max(freq.values())) >= k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
            
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        dupes = set()

        l, r = 0, 0
        while r < len(s):

            while s[r] in dupes:
                dupes.remove(s[l])
                l += 1
            
            dupes.add(s[r])
            longest = max(longest, len(dupes))
            r += 1
        return longest


        
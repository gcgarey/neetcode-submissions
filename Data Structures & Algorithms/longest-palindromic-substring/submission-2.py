class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(len(s)):
            l, r = i-1, i+1
            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > len(res):
                    res = s[l:r+1]
                l -=1
                r += 1

            # even length
            r = i + 1
            l = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res
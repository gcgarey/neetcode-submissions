class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx, reslen = 0, 0

        for i in range(len(s)):
            # odd length 
            r, l = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
            
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    residx = l

                l -= 1
                r += 1
                

            # even length
            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if (r - l + 1) > reslen:
                    reslen = r - l + 1
                    residx = l

                r += 1
                l -= 1
        

        return s[residx: residx + reslen]
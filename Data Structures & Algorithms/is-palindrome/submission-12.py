class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for let in s.lower():
            if let.isalnum():
                res += let
        print(res)
        return res == res[::-1]
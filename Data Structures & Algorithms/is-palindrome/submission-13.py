class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for ch in s.lower():
            if ch.isalnum():
                newString += ch
        return newString == newString[-1::-1]
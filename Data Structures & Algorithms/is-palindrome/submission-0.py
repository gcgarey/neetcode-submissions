class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for c in s:
            if c.isalnum():
                newString += c.lower()

        right = len(newString) - 1
        left = 0
        
        while left <= right: 
            if newString[left] != newString[right]:
                return False
            left += 1
            right -= 1
        return True

        
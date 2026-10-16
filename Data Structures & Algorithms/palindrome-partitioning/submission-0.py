class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def isPalindrome(word):
            l, r = 0, len(word)-1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrack(i):
            if i == len(s):
                res.append(sol.copy())
                return

            for j in range(i, len(s)):
                word = s[i:j+1]
                if isPalindrome(word):
                    sol.append(word)
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return res
        

        
        
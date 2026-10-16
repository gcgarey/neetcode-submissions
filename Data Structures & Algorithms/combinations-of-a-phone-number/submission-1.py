class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        res, sol = [], []

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(sol))
                return

            curr = mapp[digits[i]]
            for c in curr:
                sol.append(c)
                backtrack(i+1)
                sol.pop()
                
        if digits:
            backtrack(0)
        return res

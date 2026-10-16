class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(o, c):
            if o == c == n:
                res.append("".join(sol))
                return
            
            if o < n:
                sol.append("(")
                backtrack(o+1, c)
                sol.pop()

            if c < o:
                sol.append(")")
                backtrack(o, c+1)
                sol.pop()

        backtrack(0, 0)
        return res

            

        
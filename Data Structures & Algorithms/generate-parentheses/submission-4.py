class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(o, c):
            if o == c == n:
                res.append("".join(sol))
                return
            if c > o or c > n or o > n:
                return

            # add an open parenthesis
            sol.append("(")
            backtrack(o+1, c)
            sol.pop()

            # add a closed parenthesis
            sol.append(")")
            backtrack(o, c+1)
            sol.pop()

        backtrack(0, 0)
        return res

        
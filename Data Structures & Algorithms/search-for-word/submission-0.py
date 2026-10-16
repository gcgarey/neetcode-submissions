class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # horizontal or vertical
        path = set()
        
        def backtrack(r, c, w):
            if w == len(word): return True
            if (r < 0) or (c < 0) or (r >= len(board)) or (c >=     len(board[0])) or ((r, c) in path) or (board[r][c] != word[w]):
                return False

            path.add((r, c))
            res = backtrack(r+1, c, w+1) or backtrack(r-1, c, w+1) or backtrack(r, c+1, w+1) or backtrack(r, c-1, w+1)

            path.remove((r, c))
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if backtrack(row, col, 0):
                    return True
        return False
            
                    

            

        
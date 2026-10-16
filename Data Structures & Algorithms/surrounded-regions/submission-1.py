class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visited or board[r][c] == "X":
                return

            board[r][c] = "#"
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROW):
            for c in range(COL):
                if r == 0 or c == 0 or r == ROW-1 or c == COL-1:
                    dfs(r,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"




        
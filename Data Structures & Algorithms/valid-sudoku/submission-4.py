class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # count rows 
        for i in range(9):
            temp_row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in temp_row:
                    return False
                else:
                    temp_row.add(board[i][j])
        # count colums
        for i in range(9):
            temp_col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in temp_col:
                    return False
                else:
                    temp_col.add(board[j][i])
        # count squares
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in box[(r//3, c//3)]:
                    return False
                else:
                    box[(r//3, c//3)].add(board[r][c])

        return True


        
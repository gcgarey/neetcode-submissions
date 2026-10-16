class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # define rows and columns of the matrix
        ROW = len(matrix)
        COLUMN = len(matrix[-1])

        # define the left and right of the outer list
        top = 0
        bot = ROW - 1
        while top < bot:
            current_row = (top + bot) // 2
            if target > matrix[current_row][-1]:
                top += 1
            elif target < matrix[current_row][0]:
                bot -= 1
            else:
                break

        l = 0
        r = COLUMN - 1
        row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r -= 1
            else:
                l += 1
        return False
        
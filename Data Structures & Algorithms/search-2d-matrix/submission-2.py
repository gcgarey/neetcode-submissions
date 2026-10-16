class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix) - 1
        COL = len(matrix[0]) - 1

        top = 0
        bot = ROW
        while top <= bot:
            current_row = (top + bot) // 2
            if matrix[current_row][-1] < target:
                top = current_row + 1
            elif matrix[current_row][0] > target:
                bot = current_row - 1
            else:
                break

        l = 0
        r = COL
        curr_row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[curr_row][mid]:
                return True
            elif target > matrix[curr_row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
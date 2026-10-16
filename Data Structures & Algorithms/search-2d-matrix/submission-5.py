class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix)-1
        while lrow <= rrow:
            midrow = (lrow + rrow) // 2
            if target >= matrix[midrow][0] and target <= matrix[midrow][-1]:
                l, r = 0, len(matrix[midrow]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    print(mid)
                    if matrix[midrow][mid] == target:
                        return True
                    elif matrix[midrow][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            elif target < matrix[midrow][0]:
                rrow = midrow - 1
            else:
                lrow = midrow + 1
        return False
        

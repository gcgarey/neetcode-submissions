class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, visited, prevH):
            # check if position is in bounds and valid
            if r<0 or c<0 or r>=ROW or c>=COL or (r, c) in visited or prevH > heights[r][c]:
                return

            # visit all neighbors
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # top row, right column
        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROW-1, c, atlantic, heights[ROW-1][c])

        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COL-1, atlantic, heights[r][COL-1])

        for cell in atlantic:
            if cell in pacific:
                res.append(list(cell))
        return res
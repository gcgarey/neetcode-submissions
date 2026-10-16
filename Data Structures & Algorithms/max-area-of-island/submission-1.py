class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        self.res = 0

        def dfs(r, c):
            if (r < 0) or (c < 0) or (r >= ROW) or (c >= COL) or (grid[r][c] == 0):
                return 0

            grid[r][c] = 0

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1)+ dfs(r, c+1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    self.res = max(self.res, dfs(r, c))

        return self.res
        
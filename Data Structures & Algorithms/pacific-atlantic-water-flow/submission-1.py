class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited or prev > heights[r][c]:
                return

            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # Pacific: top and left
        for c in range(COL):
            dfs(0, c, pacific, 0)
            dfs(ROW-1, c, atlantic, 0)

        for r in range(ROW):
            dfs(r, 0, pacific, 0)
            dfs(r, COL-1, atlantic, 0)

        for h in pacific:
            if h in atlantic:
                res.append(h)

        return res


        
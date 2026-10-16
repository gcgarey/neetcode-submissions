class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # check cell and add fresh fruit to the queue
        def makeRotten(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or (r,c) in visited or grid[r][c] == 0:
                return
            grid[r][c] = 2
            q.append([r,c])
            visited.add((r,c))

        # add the bad fruits to the queue (point to bfs from)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
        
        # conduct the bfs to get the time
        count = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                makeRotten(r+1,c)
                makeRotten(r-1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
            if q: count += 1

        # if there is still fresh fruit: return -1, else return count
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        return count


        

        
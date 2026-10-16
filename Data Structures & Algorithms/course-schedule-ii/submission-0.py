class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        prereq = {x: set() for x in range(numCourses)} # crs: [prereqs]
        depend = {x: [] for x in range(numCourses)} # prereq: [courses]
        q = deque()

        # populate dependency/ adj list
        for crs, pre in prerequisites:
            prereq[crs].add(pre)
            depend[pre].append(crs)

        # find courses with no prereqs
        for i in range(numCourses):
            if len(prereq[i]) == 0:
                q.append(i)

        # conduct BFS
        while q:
            c = q.popleft()
            visited.add(c)
            res.append(c)

            for crs in depend[c]:
                if c in prereq[crs]:
                    prereq[crs].remove(c)
                if len(prereq[crs]) == 0:
                    q.append(crs)
        
        if len(visited) == numCourses:
            return res
        return []
        
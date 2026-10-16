class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereqs = {x: set() for x in range(numCourses)} # crs : [pre]
        depend = {x : [] for x in range(numCourses)} # pre : [crs]
        q = deque()

        # populate dependency list + prereqs set
        for crs, pre in prerequisites:
            prereqs[crs].add(pre)
            depend[pre].append(crs)

        # find course that don't have prereqs
        for i in range(numCourses):
            if len(prereqs[i]) == 0:
                q.append(i)
        print(q)
        while q:
            c = q.popleft()
            visited.add(c)

            for crs in depend[c]:
                # if that crs has no other dependencies : add to q
                if c in prereqs[crs]:
                    prereqs[crs].remove(c)
                if len(prereqs[crs]) == 0:
                    q.append(crs)


        return len(visited) == numCourses

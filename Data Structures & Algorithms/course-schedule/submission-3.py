class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        q = deque()
        prereq = {x: set() for x in range(numCourses)}
        dependents = {x: [] for x in range(numCourses)}

        # find the course with no prereqs and add to visited
        for i in range(len(prerequisites)):
            prereq[prerequisites[i][0]].add(prerequisites[i][1])
            dependents[prerequisites[i][1]].append(prerequisites[i][0])

        for j in range(len(prereq)):
            if len(prereq[j]) == 0:
                q.append(j)


        # bfs : from all courses I have taken
        while q:
            course = q.popleft()
            visited.add(course)
            # add all courses that are a prereq for to visited
            for k in dependents[course]:
                prereq[k].remove(course)
                
                if k not in visited and len(prereq[k]) == 0:
                    q.append(k)

        return len(visited) == numCourses






    
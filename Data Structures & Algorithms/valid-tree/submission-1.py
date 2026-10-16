class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connected = {x: set() for x in range(n)}
        visited = set()

        # create my adjacency graph
        for s, e in edges:
            connected[s].add(e)
            connected[e].add(s)

        # dfs to find any cycles
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for n in connected[node]:
                if n == parent:
                    continue
                if dfs(n, node) is False:
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
        
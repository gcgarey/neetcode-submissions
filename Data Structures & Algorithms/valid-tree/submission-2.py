class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {x: set() for x in range(n)}
        visited = set()

        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                
                if dfs(n, node) is False:
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        
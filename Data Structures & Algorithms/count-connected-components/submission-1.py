class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        adj = {x: set() for x in range(n)}

        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)

        def dfs(node, parent):
            if node in visited:
                return False

            print(visited)
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                
                dfs(n, node)
                    
            
            return True

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i, -1)

        return res
        
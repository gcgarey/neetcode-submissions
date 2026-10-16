"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])

        seen = {}
        while queue:
            temp = queue.popleft()
            if temp.val not in seen:
                newNode = Node(temp.val, [])
                seen[temp.val] = newNode
            else:
                newNode = seen[temp.val]
                seen[temp.val] = newNode


            for n in temp.neighbors:
                if n.val in seen:
                    newNode.neighbors.append(seen[n.val])
                else:
                    neighborNode = Node(n.val, [])
                    seen[n.val] = neighborNode
                    newNode.neighbors.append(neighborNode)
                    queue.append(n)
        return seen[node.val]


        
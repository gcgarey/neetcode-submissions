"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None : None}
        curr = head

        # fill the hashmap {OG node --> newNode}
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next

        # fill in the pointers
        curr = head
        while curr:
            newNode = nodes[curr]
            newNode.next = nodes[curr.next]
            newNode.random = nodes[curr.random]
            curr = curr.next

        return nodes[head]

        
        
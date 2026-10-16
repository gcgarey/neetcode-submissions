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
        # create a hashmap of OG node --> copy
        nodes = {None : None} 
        curr = head
        while curr:
            node = Node(curr.val)
            nodes[curr] = node
            curr = curr.next

        curr = head
        while curr:
            # copy curr.next = 
            nodes[curr].next = nodes[curr.next]
            nodes[curr].random = nodes[curr.random]
            curr = curr.next

        return nodes[head]
       
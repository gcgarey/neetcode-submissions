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
        first = head

        while first:
            nodes[first] = Node(first.val)
            first = first.next
        
        second = head 
        while second:
            newNode = nodes[second]
            newNode.next = nodes[second.next]
            newNode.random = nodes[second.random]
            second = second.next

        return nodes[head]
        
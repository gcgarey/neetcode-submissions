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
        # create hash map to map from old to copy 
        old2new = {None : None}

        # iterate through og list to create new nodes and build hashmap
        cur = head
        while cur:
            newNode = Node(cur.val)
            old2new[cur] = newNode
            cur = cur.next

        # iterate through new nodes created to set pointers (access dict)
        cur = head
        while cur:
            newNode = old2new[cur]
            newNode.next = old2new[cur.next]
            newNode.random = old2new[cur.random]
            cur = cur.next 
        
        return old2new[head]
        
        

        

        

        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# A --> B --> C     next_node = B

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define the current node and the previous node
        curr = head
        prev = None

        # iterate through the linked list. Get the next node's value
        while curr:
            next_node = curr.next
            # set the current's next value to its previous value
            curr.next = prev
            # then set the prev to the current
            prev = curr
            # then set the current to the next
            curr = next_node
        return prev

        
        

        
        
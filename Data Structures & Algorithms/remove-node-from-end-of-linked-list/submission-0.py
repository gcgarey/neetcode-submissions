# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Make a dummy node before the head
        dummy = ListNode(None, head)
        # create my first and second pointers
        first = dummy
        second = dummy

        # move first forward n times
        curr = 0
        while curr != n:
            curr += 1
            first = first.next
        
        # move both until first reaches the end
        while first.next:
            first = first.next
            second = second.next
        # second is right before the node we need to move: cut it off
        second.next = second.next.next
        
        return dummy.next

        
        
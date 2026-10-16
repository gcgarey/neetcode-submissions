# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(None, head)
        # split list into first and second half
        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next

        # reverse the second half
        second = s.next
        s.next = prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # combine the two lists back together
        first, second = head, prev
        while first and second: 
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first, second = next_first, next_second

        
         
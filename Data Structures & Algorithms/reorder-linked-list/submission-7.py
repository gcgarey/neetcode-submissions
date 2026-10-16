# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle 
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        s.next = None
        # reverse the second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Combine
        l1, l2 = head, prev
        curr = ListNode()
        while l1 and l2:
            t1, t2 = l1.next, l2.next
            curr.next = l1
            curr = curr.next
            curr.next = l2
            curr = curr.next
            l1, l2 = t1, t2
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)

        # reverse the second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # put back together
        l1, l2 = head, prev
        while l1 and l2:
            l1tmp, l2tmp = l1.next, l2.next
            l1.next = l2
            l1 = l1tmp
            l2.next = l1
            l2 = l2tmp
             

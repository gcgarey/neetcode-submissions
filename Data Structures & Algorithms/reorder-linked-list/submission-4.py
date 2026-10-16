# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        prev = None
        slow.next = prev
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        start2 = prev
        start1 = head
        while start1 and start2:
            i = start1.next
            j = start2.next
            start1.next = start2
            start2.next = i
            start1, start2 = i, j

        print(head.val)
    
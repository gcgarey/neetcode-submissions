# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       # use the fast and slow pointers to break up list
       slow = head
       fast = slow
       while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
       # reverse the second list
       second = slow.next
       slow.next = prev = None
       while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

       # integrate them back in
       first = head
       second = prev
       while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
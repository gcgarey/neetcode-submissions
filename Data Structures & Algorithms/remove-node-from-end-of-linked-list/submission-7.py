# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0 
        while curr:
            l += 1
            curr = curr.next

        if l - n == 0:
            return head.next
        
        curr = head
        for i in range(1, l):
            if l - i == n:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use the fast and slow pointers to find middle of list
        slow = head 
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #separate the lists
        second = slow.next
        prev = slow.next = None
        # Reverse the second half of the list
        while second: 
            # define temp
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        

        

        
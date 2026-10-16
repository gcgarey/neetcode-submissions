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

        # reverse the second half
        prev, curr = None, s.next
        s.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # put them together
        dummy = ListNode()
        curr = dummy
        list1, list2 = head, prev
        while list1 and list2:
            temp1, temp2 = list1.next, list2.next
            curr.next = list1
            curr = curr.next
            curr.next = list2
            curr = curr.next
            list1, list2 = temp1, temp2
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2


  
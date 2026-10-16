# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 4, 8 6 --> 2 8 4 6
        # step 1: use fast and slow to break up
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse order of the second half
        second = slow.next
        slow.next = prev = None

        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # step 3: merge back together
        first = head
        second = prev
        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            

        
        

        
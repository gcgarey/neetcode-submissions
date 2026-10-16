# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Make a node to represent the head and the linked list
        head = node = ListNode()

        # compare the values of the two linked lists (if they are populated)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        # now add on the rest of the list we didn't get to
        node.next = list1 or list2
        # return the head of the list
        return head.next
        

        


        
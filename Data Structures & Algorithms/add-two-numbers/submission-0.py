# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to return at the end
        dummy = ListNode()
        # create a current pointer to keep track of where we are
        curr = dummy
        # create a carry variable for addition reasons
        carry = 0

        # start the loop
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # add the value of the nodes from l1 and l2 + carry
            val = v1 + v2 + carry
            #update carry
            carry = val // 10
            # find the ones place
            val = val % 10
            # set the next node to the ones place
            curr.next = ListNode(val)

            # update our variables so we dont have a forever loop
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next


        

            


        
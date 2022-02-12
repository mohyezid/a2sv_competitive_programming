# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ptrslow = ptrfast = head
        count = 0

        while count != n:
                  ptrslow = ptrslow.next
                  count += 1

        if ptrslow is None:
             return head.next

        while ptrslow is not None:
                      ptrslow = ptrslow.next
                      temp = ptrfast
                      ptrfast = ptrfast.next

        temp.next = ptrfast.next

        return head

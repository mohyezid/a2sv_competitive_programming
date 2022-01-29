   # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
   value = []
        temp = head
        while temp:
            list1.append(temp.val)
            temp = temp.next
        return value == value[::-1]

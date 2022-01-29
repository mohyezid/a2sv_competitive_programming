# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = head
        two=head
        count=0
        
        while one is not None  :
                one = one.next
                 
                count+=1
        if count==1:
            return two
        middle=count//2
        count=0
        while two is not None:
            two=two.next
            count+=1
            if count>=middle:
                return two

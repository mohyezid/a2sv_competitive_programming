def findMergeNode(head1, head2):
    
    while head1 is not None:
        temp=head2
        while temp is not None:
            if head1==temp:
                return head1.data
            temp=temp.next
        
        head1=head1.next

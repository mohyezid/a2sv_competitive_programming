def removeDuplicates(llist):
    
    temp = llist
    if temp==None or temp.next==None:
        return llist
    nex=temp.next
    while nex!= None:
        if temp.data==nex.data:
            temp.next = nex.next
            nex=nex.next
        else:
            temp = temp.next
            nex = nex.next
    return llist
  

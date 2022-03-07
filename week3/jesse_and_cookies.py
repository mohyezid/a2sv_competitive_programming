def cookies(k, A):
    count=0
    heapq.heapify(A)

    
    while  k > A[0] :
        if len(A) <2:
            return -1
        y=heapq.heappop(A)
        heapq.heappush(A,y+2*heapq.heappop(A))
        
        count+=1
    
    return count

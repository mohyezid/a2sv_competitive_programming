if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
     
    arr=set(arr)
    list=list(arr)
    list.sort()
    size=len(list)
    print(list[size-2])

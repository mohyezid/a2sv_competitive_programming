def Pattern(n=int(input())):
    for i in range(2):
        print()                                 #time complexity O(n^2)
        for j in range(n):
            print("#"*(n-1)+" ",end='')
if __name__ == '__main__':
    Pattern()

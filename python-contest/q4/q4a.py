def pattern(length=int(input())):
     for i in range(1,length+1):
            for j in range(length - i):
                print(" ", end =" ")
            for m in range(1,i+1):
                print(m, end=" ")
            for n in range(1,i):
                print(i-n,end =" ")
            print()
if __name__ == '__main__':
    pattern()

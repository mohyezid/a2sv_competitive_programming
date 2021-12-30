n,x= map(int, input().split())
zipped = []
for _ in range(x):
    zipped.append( map(float, input().split()) ) 

for i in zip(*zipped): 
    print( sum(i)/len(i) )

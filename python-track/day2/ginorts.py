l = ""
e = ""
u = ""
o = ""
s=sorted(input())
for x in s:
    if x.islower():
        l+=x 
    elif x.isupper():
        u+=x
    elif int(x)%2!=0:
        o+=x
    elif int(x)%2==0:
         e+=x
 
print(l+u+o+e)

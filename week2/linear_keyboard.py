from typing import DefaultDict
 
 
testcase = int(input())#number of testcases
 
while testcase!=0 :
    letter = input()
    s = input()
    letter_map = DefaultDict(int)
    count = 0
 
    for j,k in enumerate(letter,start=1):
        letter_map[k] = j
 
    for l in range(1,len(s)):
        count += abs(letter_map[s[l]] - letter_map[s[l-1]])
    testcase-=1
    print(count)

def RomanNumChanger(roman): 
    sum=0
    previous=0
    containt={'I':  1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D' : 500,
    'M' :  1000
    }
    for i in range(len(roman)-1, -1, -1):
        if containt[roman[i]] >= previous:
            sum += containt[roman[i]]
        else:
            sum -= containt[roman[i]]
    
        previous = containt[roman[i]]
    
 
    print(sum)

if __name__ == '__main__':
    str = list(input())
    RomanNumChanger(str)

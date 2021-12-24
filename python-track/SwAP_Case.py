def swap_case(s):
    
    text=""
    for i in range(len(s)):
        if s[i].isupper():
        
            text+= s[i].lower()
        elif s[i].islower():
        
            text+=s[i].upper()
        else:
            text+=s[i]
    return text

if __name__ == '__main__':

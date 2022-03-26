class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2!=0:
            return False
        count = 0
        swap = 0
        for ch , k in zip(s,locked):
            if ch=='(':
                count += 1
            else:
                count -= 1
            if k == '0' and ch==')':
                swap += 1
            if count < 0:
                if swap == 0:
                    return False
                else:
                    count+=2
                    swap-=1
        count = 0
        swap = 0
        for  i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                count += 1
            else:
                count -= 1
            if locked[i] == '0' and s[i]=='(':
                swap += 1
            if count < 0:
                if swap == 0:
                    return False
                else:
                    count += 2
                    swap -= 1
                
                
                
        return True
            
         
         
        
        
#         s=list(s)
#         opening='('
#         close=')'
#         if len(s)==1:
#             return False

#         for i in range(len(s)):
#             if i==0 and locked[i]=='0':
#                 if s[i+1]==close:
#                     s[i]= opening
#                 else:
#                     s[i]=')'
                
#             elif locked[i] =='0' and s[i-1]==close:
#                 s[i]='('
#             elif locked[i] =='0' and s[i-1]==opening:
#                 s[i]=')'
#             elif  locked[i]=='1' and s[i]==close:
#                 if s[i-1]==')':
#                     return False
                
#             elif  locked[i]=='1' and s[i]==opening:
#                 if s[i-1]=='(':
#                     return False
                
            
#         return True   

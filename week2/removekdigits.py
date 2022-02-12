class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count = 0
        stri = "" 
        stack =  []
        for i in num:
            while count < k and stack and i < stack[-1]:
                count += 1
                stack.pop()
             
            if not stack and i!= '0': 
                stack.append(i)
            elif stack :
                stack.append(i)
         
        n = len(stack)-(k-count)
         
        if n <= 0:
            return "0"
 

        for i in range(n):
            stri+= stack[i]
             
        
        
        return stri  
        

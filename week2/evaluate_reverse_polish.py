class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for value in tokens:
            if value not in "+/-*":
                
                    stack.append(int(value))
                

            else:
                a=stack.pop()
                b=stack.pop()
                if value=='+':
                    result=a+b
                elif value=='*':
                    result=a*b
                elif value=='/':
                    result=int(b/a)
                elif value=='-':
                    result=b-a
                stack.append(result)
        return stack[-1]
        

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close=")]}"

        output=False
        if len(s)%2!=0:
             return output
        for i in s:
            if i not in close:
                stack.append(i)
            elif i== close[0]:
                if len(stack)!=0:
                    current=stack.pop()
                    if current!='(':
                         return output
                else:
                     return output
            elif i== close[1]:
                if len(stack)!=0:
                    current=stack.pop()
                    if current!='[':
                         return output
                else:
                     return output
            elif i== close[2]:
                if len(stack)!=0:
                    current=stack.pop()
                    if current!='{':
                         return output
                else:
                     return output
        if len(stack)==0 :
            output=True
        else:
             output=False
        return output

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        stack2=[]
        for i in s:
            if i=='#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        for i in t:
            if i=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        if stack2==stack:
             return True
        else:
             return False

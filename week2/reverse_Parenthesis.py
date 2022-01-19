class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        n=len(s)

        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                reverse_string=s[stack[-1]:i+1]
                s=s[:stack[-1]]+reverse_string[::-1]+s[i+1:]
                stack.pop()
        s=s.translate({ord(c):None for c in ")("})
        return s

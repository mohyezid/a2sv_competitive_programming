class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and d[stack[-1]] >i:
                p=stack.pop()
                seen.remove(p)
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)

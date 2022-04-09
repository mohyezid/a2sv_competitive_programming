class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome=list(palindrome)
        i = 0
        C=Counter(palindrome)
        if len(palindrome)==1:
            return ""
        
        if 'a' in C and len(palindrome)-C['a'] in [0,1]:        
            palindrome[-1]='b'
             
            
        else:
            while i < len(palindrome):
                if palindrome[i]!='a':
                    palindrome[i]='a'
                    break
                i += 1
         
        
        return "".join(palindrome)

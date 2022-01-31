class Solution:
    def sortSentence(self, s: str) -> str:
        
         
        def lastChar(s):
            return s[-1]
        
         
        def removeLast(s):
            return s[:-1]
        
         
        words = s.split(" ")
        
        
        words.sort(key=lastChar)
        
        
        last = map(removeLast, words)
        
         
        return " ".join( last)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        se =set()
       
        i = 0
        j = 9
         
        while j <len(s):
            
            if s[i:j+1] in se:
                res.append(s[i:j+1])
                i+=1
                j+=1
            elif s[i:j+1] not in se:
                se.add(s[i:j+1])
                i+=1
                j+=1
                 
        return  list(set(res))
            

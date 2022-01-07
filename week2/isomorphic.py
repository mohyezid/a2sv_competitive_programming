class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        s1 = set()
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if x in dictionary:
                if dictionary[x] != y:
                    return False
 
         
            else:
             
                if y in s1:
                    return False
                dictionary[x] = y
                s1.add(y)
              
        return True

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     
        
        
        l=0
        r=0
        string=[0]*26
        mlength =  0
        while r < len(s):
            string[ord(s[r])-65]+=1 
         
             
                 
            if  (r-l+1) - max(string) > k:
                string[ord(s[l])-65]-=1
                l+=1
             
                
            mlength = max(mlength,r-l+1)
            r += 1
                 
                
        return mlength 

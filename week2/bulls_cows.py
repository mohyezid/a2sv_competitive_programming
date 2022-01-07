class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret=[i for i in secret]
        guess=[i for i in guess]
 
        i=0
        bulls=0
        cows=0
        while i < len(secret):
    
            if  secret[i] == guess[i]:
                bulls+=1
                secret.pop(i)
                guess.pop(i)
            else:
                i+=1
        for i in range(len(guess)):
            if guess[i] in secret:
                cows+=1
                secret.pop(secret.index(guess[i]))
  
        return str(bulls)+"A"+str(cows)+"B"

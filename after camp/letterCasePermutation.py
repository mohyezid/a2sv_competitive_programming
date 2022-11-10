class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        ans = []
        def dfs(index,prev):
             
            if index == len(s)-1:
              
                res.append(prev)
                ans.append("".join(res[1:].copy()))
            if index+1 < len(s) and s[index+1]  not in "0123456789":
                
                res.append(prev)
                dfs(index+1,s[index+1].lower())
               
                res.pop()
                dfs(index+1,s[index+1].upper())
                
                res.pop()
            if index+1 < len(s) and s[index+1] in '0123456789':
                res.append(prev)
                dfs(index+1,s[index+1])
                res.pop()
        dfs(-1,'-1')   
        return ans
                

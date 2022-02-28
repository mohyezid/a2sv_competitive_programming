class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
         


        d={}
        i=0
        while i < len(edges):
            j=0
            while j <2:
                if edges[i][j] in d.keys():
                    d[edges[i][j]]=d[edges[i][j]]+1
                    
                else:
                    d[edges[i][j]]=1
                j+=1
            i+=1
        for i,val in d.items():
            if val==len(edges):
                return i
        

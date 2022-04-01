class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        h ={}
         
        for i in range(0,len(nums),2):
            if nums[i] in h:
                h[nums[i]] +=1
            else:
                h[nums[i]] = 1
        h2 = {}
        for i in range(1,len(nums),2):
            if nums[i] in h2:
                h2[nums[i]] +=1
            else:
                h2[nums[i]] = 1
        hv1=sum(h.values())
        hv2=sum(h2.values())
        hm = [(k,h[k]) for k in h.keys()]
        hm2 = [(k,h2[k]) for k in h2.keys()]
        hm = sorted(hm, key= lambda x: x[1],reverse = True)
        hm2 = sorted(hm2, key= lambda x: x[1],reverse = True)
        if len(hm2) == 0:
            return 0
        if hm2[0][0] == hm[0][0]:
            poss = 10 ** 10
            if len(hm2) > 1:
                poss = min(poss, (hv1 - hm[0][1]) + (hv2 - hm2[1][1]))
            else:
                poss = min(poss, (hv1 - hm[0][1]) + (hv2))
            if len(hm) > 1:
                poss = min(poss, (hv1 - hm[1][1]) + (hv2 - hm2[0][1]))
            else:
                poss = min(poss, (hv1) + (hv2 - hm2[0][1]))
            return poss
        else:
            return (hv1 - hm[0][1]) + (hv2 - hm2[0][1])
            

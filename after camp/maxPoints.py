class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        a = defaultdict(set)
        def helper(p1,p2):
            if p2[1]==p1[1]:
                return 0,p1[1]
            if   p2[0]==p1[0]:
                return p1[0],None
            slope = (p2[1]-p1[1])/(p2[0]-p1[0])
            y = p1[1]-(slope*p1[0])
            return slope,y
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                p1 = points[i]
                p2 = points[j]
                lines = helper(p1,p2)
                a[lines].add(i)
                a[lines].add(j)
        ans  = 0
        for j in a:
            ans = max(ans,len(a[j]))
        return ans
                

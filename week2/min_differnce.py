class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minimum=1440
        time=[]
        for i in range(len(timePoints)):
            if timePoints[i]=='00:00':
                time.append(minimum)
            
            else:
                h,m=timePoints[i].split(':')
                time.append(int(m)+int(h)*60)
        time.sort()
        for i in range(len(time)-1):
            
            if time[i+1]-time[i] < minimum:
                minimum=time[i+1]-time[i]
        t=time[0]-time[-1]+1440 
        return t if t>0 and t<minimum else minimum

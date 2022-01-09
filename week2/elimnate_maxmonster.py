class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        count=0
 
        minute=[  dist[i]/speed[i] for i in range(len(dist))] 
        minute.sort()
        for min in range(len(minute)):
            if minute[min]>min:
                count+=1
            else:
                break
        return count

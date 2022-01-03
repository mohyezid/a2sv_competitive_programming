class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        excepted=[]
        count=0
        for i in heights:
            excepted.append(i)
        heights.sort()
        for i in range(len(heights)):
            if heights[i]!=excepted[i]:
                count+=1
        return(count)

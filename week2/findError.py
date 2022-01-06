class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        track_num={}
        for i in range(1,len(nums)+1):
            track_num[i]=0
        for item in nums:
            track_num[item]+=1
 
        duplicate_index=list(track_num.values()).index(2)
        duplicate= duplicate_index +1
        missing_index=list(track_num.values()).index(0)
        missing= missing_index +1
        return[duplicate,missing]

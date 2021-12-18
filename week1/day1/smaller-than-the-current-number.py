class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            
            size=len(nums) 
            list = [0] * size  
            for i in range(size):
                count=0
                for j in range(size) :
                     if nums[i] > nums[j]:
                            count=count+1
                list[i]=count
            return list

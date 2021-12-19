class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list=[]
        size=len(nums)
        for i in range(size):
             
            minindex=i 
            for j in range(i+1,size):
                if nums[j]<=nums[minindex]:
                    minindex=j
            temp=nums[i]
            nums[i]=nums[minindex]
            nums[minindex]=temp
        for i in range(size):
            if nums[i]==target:
                list.append(i)
        return list
            
        
        

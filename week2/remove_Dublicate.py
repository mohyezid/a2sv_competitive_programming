class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
         
        n=len(nums)
        if n==0 or n==1:
            
            return n;
        end=nums[n-1]
        count=0
        for i in range(n-1):
             if nums[i]!=nums[i+1]:
                nums[count]=nums[i]
                count+=1
                
        nums[count]= end
        count+=1
        return count

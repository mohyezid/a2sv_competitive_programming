class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        i = 0
        j = 0
        n = len(nums)
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
             
        for i in range(i,n,1):
            nums[i]= 0
        

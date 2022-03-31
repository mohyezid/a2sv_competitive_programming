class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        Total =  len(nums)
        small = []
        big = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                big.append(nums[i])
            elif nums[i] < pivot:
                small.append(nums[i])
         
            
        for i in range(Total-len(small+big)):
            small.append(pivot)
         
        return small+big

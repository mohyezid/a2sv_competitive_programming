class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major , count = 0,0
        for i in nums:
            if count == 0:
                major = i
             
            if major == i:
                count += 1
            else:
                count-=1
        return major
#         d = {}
    
#         for i in range(len(nums)):
#             if nums[i] not in d:
#                 d[nums[i]] = 1
#             else:
#                 d[nums[i]] += 1
#         for k,v in d.items():
#             if v > len(nums)//2:
#                 return k
        
         

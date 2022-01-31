class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest=""
        result=""
         
        nums= list(map(str,nums))
        while nums:
            for i in nums:
                if not  largest:
                     largest=i
                else:
                    
                    if i+ largest> largest+i:
                         largest=i
            result+=largest
            nums.remove(largest)
            largest=""
        return result if  result[0]!="0" else "0"

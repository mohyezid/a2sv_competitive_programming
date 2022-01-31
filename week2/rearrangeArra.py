class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
            index =1 
            while index< len(nums)-1:
		
			 
                if (nums[index-1] +nums[index+1])/2 == nums[index]:
                    nums[index+1], nums[index] = nums[index], nums[index+1]


                    if index>1:
                        index-=1

                else:
                    index+=1
            return nums

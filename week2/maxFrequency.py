class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        maxi = -1

        left = 0
        usage = 0
        for right, num in enumerate(nums):
            usage += (right-left)*(nums[right]-nums[right-1])
            while left < right and usage > k:
                usage -= (nums[right]-nums[left])
                left += 1
            maxi = max(maxi, right-left+1)
        return maxi
       

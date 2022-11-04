class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
         
        prev, current = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            new_current = max(current, nums[i] + prev)
            prev, current = current, new_current
        return current

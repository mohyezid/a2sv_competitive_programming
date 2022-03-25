class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)-1):
            L =  nums[i]
            S =  nums[i]
            for j in range(i+1,len(nums)):
                L = max(L,nums[j])
                S = min(S,nums[j])
                total += L-S
        return total

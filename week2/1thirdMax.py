class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        number = set(nums)
        if len(number) < 3:
            return sorted(number)[-1]
        else:
            return sorted(number)[-3]
         

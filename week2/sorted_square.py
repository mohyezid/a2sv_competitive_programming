class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output=sorted([i**2 for i in nums])
        return output

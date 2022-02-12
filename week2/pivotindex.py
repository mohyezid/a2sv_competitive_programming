class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
            total = sum(nums)
            presum = 0
            count=0
            for i in nums:
                if presum == total - presum - i:
                    return count
                presum += i
                count+= 1

            return -1

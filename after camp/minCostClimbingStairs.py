class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0]*(len(cost))
        arr[-1] , arr[-2] = cost[-1],cost[-2]
        for i in range(len(cost)-3,-1,-1):
            arr[i]=min( arr[i+1],arr[i+2])+cost[i]
        return min(arr[0],arr[1])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost=[cost[0],cost[1]]
        print(min_cost)
        for i in range(2,len(cost)):
            if cost[i]+min_cost[i-1]>cost[i]+min_cost[i-2]:
                min_cost.append(cost[i]+min_cost[i-2])
            else:
                min_cost.append(cost[i]+min_cost[i-1])

        
        return min_cost[-1] if min_cost[-1]<min_cost[-2] else min_cost[-2]

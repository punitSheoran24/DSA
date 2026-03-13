class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost=[cost[0],cost[1]]
        print(min_cost)
        for i in range(2,len(cost)):
            min_cost.append(min(min_cost[i-1],min_cost[i-2])+cost[i])
        return min(min_cost[-1],min_cost[-2])

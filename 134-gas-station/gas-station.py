class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        i = 0
        for j in range(len(gas)):
            total += gas[j] - cost[j]
            if total < 0:
                total = 0
                i = j + 1
        return i

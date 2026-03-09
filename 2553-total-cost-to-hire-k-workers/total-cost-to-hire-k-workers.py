import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        lst = []
        res = 0
        i = 0
        j = len(costs) - 1
        while i < candidates:
            heapq.heappush(lst, (costs[i], i))
            i += 1
        while j >= len(costs) - candidates and j >= i:
            heapq.heappush(lst, (costs[j], j))
            j -= 1

        for x in range(k):
            val, idx = heapq.heappop(lst)
            res += val
            if idx < i:
                if i<=j:
                    heapq.heappush(lst, (costs[i], i))
                    i += 1
            else:
                if j >= i:
                    heapq.heappush(lst, (costs[j], j))
                    j -= 1

           

        return res
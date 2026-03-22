class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices) - 1):
            if prices[i] > buy and prices[i] > prices[i + 1]:
                profit += prices[i] - buy
                buy = prices[i + 1]
            elif prices[i] < buy:
                buy = prices[i]
        return prices[-1] - buy + profit if prices[-1] - buy > 0 else profit
class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        stack = []
        n = len(temp)
        res = [0] * n
        for i in range(n):
            while stack and temp[stack[-1]] < temp[i]:
                index=stack.pop()
                res[index] = i - index
            stack.append(i)
        return res
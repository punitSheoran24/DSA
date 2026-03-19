class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        stack = []
        n = len(temp)
        res = [0] * n

        for i in range(n):
            j = len(stack)
            while stack and temp[stack[j - 1]] < temp[i]:
                res[stack[j - 1]] = i - stack[j - 1]
                stack.pop()
                j -= 1
            stack.append(i)

        return res
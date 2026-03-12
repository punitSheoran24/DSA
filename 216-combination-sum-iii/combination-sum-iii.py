class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtracking(k, lst, i):
            if sum(lst) == n and k == 0:
                res.append([x for x in lst])
            if k == 0:
                return
            for num in range(i + 1, 10):
                lst.append(num)
                backtracking(k - 1, lst, num)
                lst.pop()

        backtracking(k, [], 0)
        return res

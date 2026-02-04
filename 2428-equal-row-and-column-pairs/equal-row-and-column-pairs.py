class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        dic = {}
        for i in range(len(grid)):
            if str(grid[i]) in dic:
                dic[str(grid[i])] += 1
            else:
                dic[str(grid[i])] = 1
        res = 0
        for i in range(len(grid)):
            lst = []
            for j in range(len(grid)):
                lst.append(grid[j][i])
            if str(lst) in dic:
                res += dic[str(lst)]

        return res

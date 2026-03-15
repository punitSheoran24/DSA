class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        lst = [0] * col
        lst[0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    lst[j] = 0
                elif j > 0:
                    lst[j] = lst[j] + lst[j - 1]
        return lst[-1]
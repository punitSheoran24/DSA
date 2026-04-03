class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n1, n2 = len(matrix), len(matrix[0])
        rows = [False] * n1
        cols = [False] * n2

        for i in range(n1):
            for j in range(n2):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(n1):
            for j in range(n2):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
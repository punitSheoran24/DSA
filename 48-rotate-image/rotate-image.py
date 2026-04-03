class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        left, right = 0, n - 1
        c1, c2, c3, c4 = [left, left], [left, right], [right, right], [right, left]
        while left < right:
            c1, c2, c3, c4 = [left, left], [left, right], [right, right], [right, left]
            while c1[1] < right:
                (
                    matrix[c1[0]][c1[1]],
                    matrix[c2[0]][c2[1]],
                    matrix[c3[0]][c3[1]],
                    matrix[c4[0]][c4[1]],
                ) = (
                    matrix[c4[0]][c4[1]],
                    matrix[c1[0]][c1[1]],
                    matrix[c2[0]][c2[1]],
                    matrix[c3[0]][c3[1]],
                )
                c1[1] += 1
                c2[0] += 1
                c3[1] -= 1
                c4[0] -= 1
            left += 1
            right -= 1

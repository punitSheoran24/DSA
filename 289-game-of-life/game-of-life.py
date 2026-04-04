class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        # 0 | 0 | 0
        # 1 | 0 | 1
        # 0 | 1 | 2
        # 1 | 1 | 3
        rows = len(board)
        cols = len(board[0])

        def helper(r, c):
            count = 0
            for row in range(r - 1, r + 2):
                for col in range(c - 1, c + 2):
                    if (row == r and col == c) or row < 0 or col < 0 or row == rows or col == cols:
                        continue
                    if board[row][col] in [1, 3]:
                        count += 1
            return count

        for i in range(rows):
            for j in range(cols):
                c = helper(i, j)
                if board[i][j]:
                    if c in [2, 3]:
                        board[i][j] = 3
                elif c==3:
                    board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1

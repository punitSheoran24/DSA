from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(n):
            grid = set()
            for j in range((i // 3) * 3, 3 + (i // 3) * 3):
                for k in range((i % 3) * 3, 3 + ((i % 3) * 3)):
                    if board[j][k] == '.':
                        continue
                    if board[j][k] in rows[j]:
                        return False
                    if board[j][k] in cols[k]:
                        return False
                    if board[j][k] in grid:
                        return False
                    grid.add(board[j][k])
                    rows[j].add(board[j][k])
                    cols[k].add(board[j][k])
        return True

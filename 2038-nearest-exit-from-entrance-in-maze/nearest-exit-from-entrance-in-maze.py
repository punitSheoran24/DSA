from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        q = deque()
        q.append([entrance, 0])
        visited = set()
        while q:
            [i, j], step = q.popleft()
            if (i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[0]) - 1) and [i, j] != entrance:
                return step
            if (i, j) not in visited:
                if i - 1 >= 0 and maze[i - 1][j] == '.':
                    q.append([[i - 1, j], step + 1])
                if i + 1 < len(maze) and maze[i + 1][j] == '.':
                    q.append([[i + 1, j], step + 1])
                if j - 1 >= 0 and maze[i][j - 1] == '.':
                    q.append([[i, j - 1], step + 1])
                if j + 1 < len(maze[0]) and maze[i][j + 1] == '.':
                    q.append([[i, j + 1], step + 1])
                visited.add((i, j))

        return -1
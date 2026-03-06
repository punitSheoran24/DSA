from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange=set()
        rotten=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    orange.add((i,j))
                elif grid[i][j]==2:
                    rotten.append([i,j])
                    
        
        q=deque()
        if not rotten and not orange:
            return 0
        if not rotten and orange:
            return -1
        for r in rotten:
            q.append([r,0])
        while q:
            [i,j],min=q.popleft()
            if not orange:
                if q:
                    i=q.pop()
                    return i[1]
                return min
            if (i+1,j) in orange:
                q.append([[i+1,j],min+1])
                orange.remove((i+1,j))
            if (i-1,j) in orange:
                q.append([[i-1,j],min+1])
                orange.remove((i-1,j))
            if (i,j+1) in orange:
                q.append([[i,j+1],min+1])
                orange.remove((i,j+1))
            if (i,j-1) in orange:
                q.append([[i,j-1],min+1])
                orange.remove((i,j-1))
            
            



        return -1

        
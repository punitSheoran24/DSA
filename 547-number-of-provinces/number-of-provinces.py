class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dsf(i):
            self.visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j]==1  and j not in self.visited:
                    dsf(j)



        province=0
        self.visited=set()
        n=len(isConnected)
        for i in range(n):
            if i not in self.visited:
                province+=1
                dsf(i)
        return province

        
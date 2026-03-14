class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lst=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                lst[j]=lst[j]+lst[j-1]
        

        return lst[-1]
        
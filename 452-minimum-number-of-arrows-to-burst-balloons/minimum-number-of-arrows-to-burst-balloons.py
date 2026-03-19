class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        lst=sorted(points,key= lambda x : x[0])
        arrow=1
        r=lst[0][1]
        for i,j in lst[1:]:
            if i>r:
                arrow+=1
                r=j
            else:
                r=min(r,j)


        return arrow
        
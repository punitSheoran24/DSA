class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]<=height[j]:
                max_water=max(height[i]*(j-i),max_water)
                i+=1
            elif height[i]>height[j]:
                max_water=max(height[j]*(j-i),max_water)
                j-=1
        return max_water

                

 
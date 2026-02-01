class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum=sum(nums[:k])
        current_sum=total_sum
        i=1
        for j in range(k,len(nums)):
            current_sum+=nums[j]-nums[i-1]
            i+=1
            total_sum=max(total_sum,current_sum)
        
        return total_sum/k




        
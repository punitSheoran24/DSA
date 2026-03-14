class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)

        prev2=0
        prev1=0
        for n in nums:
            cur=max(prev1,prev2+n)
            prev2=prev1
            prev1=cur
        return prev1


        
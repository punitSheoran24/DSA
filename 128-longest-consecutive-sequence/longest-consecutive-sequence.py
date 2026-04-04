class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=set(nums)
        longest=0
        for h in hash:
            if (h-1) not in hash:
                count=1
                while h+count in hash:
                    count+=1
                longest=max(longest,count)
        return longest

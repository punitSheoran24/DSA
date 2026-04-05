class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        res = []
        i = j = nums[0]
        for idx, num in enumerate(nums):
            if num + 1 in nums:
                j = num + 1
            else:
                if i == j:
                    res.append(str(i))
                else:
                    res.append(f"{i}->{j}")
                if idx + 1 < len(nums):
                    i = nums[idx + 1]
                    j = i
        return res
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        res = 0
        while i <= j:
            while i < j and j >= 0 and nums[j] == val:
                res += 1
                j -= 1
            if nums[i] == val:
                res += 1
                nums[i] = nums[j]
                nums[j] = val
                j -= 1
            i += 1
        return len(nums) - res

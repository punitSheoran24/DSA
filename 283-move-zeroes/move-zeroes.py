class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[n] == 0:
                nums[i], nums[n] = nums[n], nums[i]
                n += 1

            if nums[n] != 0:
                n += 1

        return nums
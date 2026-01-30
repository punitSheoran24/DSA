class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = None
        for i in range(len(nums)):
            if nums[i] == 0 and n is None:
                n = i
            elif nums[i] != 0 and n is not None:
                nums[i], nums[n] = nums[n], nums[i]
                n += 1

        return nums
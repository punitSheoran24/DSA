class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        if 1 not in nums:
            return 0
        i = j = 0
        last_zero = i
        longest_ones = 0
        n = 1
        while j < len(nums):
            if nums[j] == 0 and n == 0:
                longest_ones = max(longest_ones, (j - i) - 1)
                i = last_zero + 1
                n += 1
            if nums[j] == 0 and n == 1:
                last_zero = j
                n -= 1
            j += 1
        if n == 1:
            longest_ones = max(longest_ones, j - i)
        elif n == 0:
            longest_ones = max(longest_ones, (j - i) - 1)

        return longest_ones

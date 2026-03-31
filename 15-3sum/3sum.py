class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while nums[i] <= 0 and i < n - 2:
            j, k = i + 1, n - 1
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
            i += 1
        return res
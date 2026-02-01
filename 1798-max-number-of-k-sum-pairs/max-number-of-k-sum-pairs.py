class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        operation = 0
        map = {}

        for num in nums:
            diff = k - num
            if diff in map:
                operation += 1
                if map[diff] == 1:
                    del map[diff]
                else:
                    map[diff] -= 1

            else:
                if num in map:
                    map[num] += 1
                else:
                    map[num] = 1

        return operation
# import math


# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
#         k = [x for x in range(1, max(piles) + 1)]
#         i, j = 1, len(k)
#         res = j
#         while i <= j:
#             mid = i+(j-i) // 2
#             count = 0
#             for ele in piles:
#                 count += math.ceil(ele / mid)
#             if count <= h:
#                 res = min(res, mid)
#                 j = mid - 1
#             else:
#                 i = mid + 1

#         return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2
            hours = sum((p + mid - 1) // mid for p in piles)

            if hours <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
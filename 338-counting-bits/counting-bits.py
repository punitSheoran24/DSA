# class Solution:
#     def countBits(self, n: int) -> list[int]:
#         def helper(n):
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 1
#             binary = format(n, 'b')
#             return 1 + helper(int(binary[1:], 2))

#         res = []
#         for i in range(n + 1):
#             res.append(helper(i))
#         return res
class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0, 1]
        prev, cur = 0, 2
        for i in range(2, n + 1):
            binary = format(i, 'b')
            if cur != len(binary):
                cur = len(binary)
                prev = 0
            res.append(1 + res[prev])
            prev += 1
        return res